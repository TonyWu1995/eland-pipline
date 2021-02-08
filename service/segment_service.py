import logging

from mongoengine import Q
import time
from constant.age import Age
from constant.gender import Gender
from service.eland_criteria_builder import ElandCriteriaBuilder
from service.eland_mongo_service import ElandDataMongoService

log = logging.getLogger(__name__)


class GenerateSegmentService:

    def __init__(self, mongo_repo: ElandDataMongoService):
        self.__mongo_repo = mongo_repo

    def generate(self, config):
        log.debug("generate() config={}".format(config))
        from_timestamp, to_timestamp = self.__calc_from_timestamp_and_to_timestamp(config['day'])
        criteria_query = ElandCriteriaBuilder().build(config['criteria_key'], config['value'], from_timestamp,
                                                      to_timestamp)
        log.debug("generate() criteria_query={}".format(criteria_query))
        print(criteria_query)
        # TODO
        # self.__mongo_repo.find_all_by_query_only("test_aggregate", Q(**criteria_query), "uuid",
        #                                          "update_at")
        # print(self.__calc_eland_data_collection_name_list(2))
        # print(self.__mongo_repo.list_collection_names())
        # self.__mongo_repo.find_all_by_query_only()
        pass

    def __calc_from_timestamp_and_to_timestamp(self, days):
        one_day_second = 86400
        to_timestamp = int(time.time()) - 2 * one_day_second
        from_timestamp = to_timestamp - one_day_second * days
        return from_timestamp, to_timestamp
