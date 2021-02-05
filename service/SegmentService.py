import datetime
import logging
import time

from repo.eland_mongo_repo import ElandDataMongoRepo

log = logging.getLogger(__name__)


class GenerateSegmentService:

    def __init__(self, mongo_repo: ElandDataMongoRepo):
        self.__mongo_repo = mongo_repo
        pass

    def generate(self, config):
        log.info("generate() config={}".format(config))
        print(self.__calc_eland_data_collection_name_list(2))
        # print(self.__mongo_repo.list_collection_names())
        # self.__mongo_repo.find_all_by_query_only()
        pass

    def __calc_eland_data_collection_name_list(self, days):
        one_day_second = 86400
        from_timestamp = int(time.time()) - 2 * one_day_second
        to_timestamp_str = datetime.datetime.fromtimestamp(from_timestamp - days * one_day_second).strftime(
            "%Y%m%d")
        from_timestamp_str = datetime.datetime.fromtimestamp(from_timestamp).strftime("%Y%m%d")
        return [str(date) for date in range(int(to_timestamp_str), int(from_timestamp_str))]
