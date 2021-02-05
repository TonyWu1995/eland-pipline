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
        print(self.__calc_time(config["day"]))
        print(self.__mongo_repo.list_collection_names())
        # self.__mongo_repo.find_all_by_query_only()
        pass

    #TODO
    def __calc_time(self, days):
        one_day_second = 86400
        today_timestamp = int(time.time()) - 2 * one_day_second
        print(datetime.datetime.fromtimestamp(today_timestamp).strftime("%Y%m%d"))
        return datetime.datetime.fromtimestamp(today_timestamp - days * one_day_second).strftime("%Y%m%d")
