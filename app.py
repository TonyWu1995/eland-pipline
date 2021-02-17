import logging
import sys
from logging.config import fileConfig

from config.config_loader import load_yml_config, load_json_config
from config.file_config import FileConfig
from config.mongodb_config import MongoDBConfig
from config.mysql_config import MysqlConfig
from config.segment_config import SegmentConfig
from constant.algo_type import AlgoType
from ml.algo.kmean_model import KmeanModel
from service.calc_segment_service import CalcSegmentService
from service.eland_criteria_builder import ElandCriteriaBuilder
from service.eland_member_mapping_service import ElandMemberMappingService
from service.eland_mongo_service import ElandDataMongoService
from service.export_segment_service import ExportSegmentService
from service.generate_segment_service import GenerateSegmentService

logging.config.fileConfig('./logging_config.ini', disable_existing_loggers=False)
log = logging.getLogger(__name__)


def main(yml_conf_file_path, json_conf_file_path):
    log.info("main() conf_file_path={}".format(yml_conf_file_path, json_conf_file_path))
    eland_data_mongo_service = ElandDataMongoService(
        MongoDBConfig.build(load_yml_config(yml_conf_file_path, "mongodb")))
    eland_member_mapping_service = ElandMemberMappingService(
        MysqlConfig.build(load_yml_config(yml_conf_file_path, "mysql")))
    segment_config_list = SegmentConfig.build_list(load_json_config(json_conf_file_path)['segment'])

    calc_ml_service = CalcSegmentService(strategy_dict={AlgoType.KMEAN: KmeanModel()})
    generate_segment_service = GenerateSegmentService(eland_data_mongo_service, eland_member_mapping_service,
                                                      ElandCriteriaBuilder(), calc_ml_service)
    export_segment_service = ExportSegmentService(
        (FileConfig.build(load_yml_config(yml_conf_file_path, "file-config"))))
    for config in segment_config_list:
        try:
            ctid_list = generate_segment_service.generate(config)
            export_segment_service.save(config.export_file_name, ctid_list)
        except Exception as e:
            log.error(e)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        main('./conf/application.yml', './conf/config.json')
