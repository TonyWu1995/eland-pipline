import logging
from logging.config import fileConfig

from config.config_loader import load_yml_config, load_json_config
from config.mongodb_config import MongoDBConfig
from config.mysql_config import MysqlConfig
from config.segment_config import SegmentConfig
from constant.algo_type import AlgoType
from ml.algo.kmean_model import KmeanModel
from service.calc_segment_service import CalcSegmentService
from service.eland_criteria_builder import ElandCriteriaBuilder
from service.eland_member_mapping_service import ElandMemberMappingService
from service.eland_mongo_service import ElandDataMongoService
from service.generate_segment_service import GenerateSegmentService

logging.config.fileConfig('./logging_config.ini', disable_existing_loggers=False)
log = logging.getLogger(__name__)


def main():
    log.info("main() start")
    eland_data_mongo_service = ElandDataMongoService(
        MongoDBConfig.build(load_yml_config("./conf/application.yml", "mongodb")))
    eland_member_mapping_service = ElandMemberMappingService(
        MysqlConfig.build(load_yml_config("./conf/application.yml", "mysql")))
    segment_config_list = SegmentConfig.build_list(load_json_config("./conf/config.json")['segment'])

    calc_ml_service = CalcSegmentService(strategy_dict={AlgoType.KMEAN: KmeanModel()})
    segment_service = GenerateSegmentService(eland_data_mongo_service, eland_member_mapping_service,
                                             ElandCriteriaBuilder(), calc_ml_service)
    for config in segment_config_list:
        segment_service.generate(config)
    pass


if __name__ == '__main__':
    main()
