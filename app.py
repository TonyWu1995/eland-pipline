import logging
from logging.config import fileConfig

from config.config_loader import load_yml_config, load_json_config
from config.mongodb_config import MongoDBConfig
from config.segment_config import SegmentConfig
from constant.algo_type import AlgoType
from ml.algo.kmean_model import KmeanModel
from ml.calc_ml_service import CalcMLService
from service.eland_criteria_builder import ElandCriteriaBuilder
from service.eland_mongo_service import ElandDataMongoService
from service.segment_service import GenerateSegmentService

logging.config.fileConfig('./logging_config.ini', disable_existing_loggers=False)
log = logging.getLogger(__name__)


def main():
    log.info("main() start")
    mongo_repo = ElandDataMongoService(MongoDBConfig.build(load_yml_config("./conf/application.yml", "mongodb")))
    segment_config_list = SegmentConfig.build_list(load_json_config("./conf/config.json")['segment'])

    calc_ml_service = CalcMLService(strategy_dict={AlgoType.KMEAN: KmeanModel()})
    segment_service = GenerateSegmentService(mongo_repo, ElandCriteriaBuilder(), calc_ml_service)
    for config in segment_config_list:
        segment_service.generate(config)
    # for config in segment_config['segment']:
    #     print(config['key'])
    #     print(config['algo'])
    #     print(config['day'])
    # print(segment_config)
    pass


if __name__ == '__main__':
    main()
