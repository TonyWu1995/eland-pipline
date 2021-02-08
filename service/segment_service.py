import logging

from mongoengine import Q

from service.eland_mongo_service import ElandDataMongoService

log = logging.getLogger(__name__)


class GenerateSegmentService:

    def __init__(self, mongo_repo: ElandDataMongoService):
        self.__mongo_repo = mongo_repo
        pass

    def generate(self, config):
        log.info("generate() config={}".format(config))
        # q = {"uuid": "74FAE51867348A0E2AACE2D0CF140C83"}
        q = {"gender_tag": 2}
        print(self.__mongo_repo.find_all_by_query_only("test_aggregate", Q(**q), "uuid"))
        # print(self.__calc_eland_data_collection_name_list(2))
        # print(self.__mongo_repo.list_collection_names())
        # self.__mongo_repo.find_all_by_query_only()
        pass



    # TODO rm check if un use
    # def __calc_eland_data_collection_name_list(self, days):
    #     one_day_second = 86400
    #     from_timestamp = int(time.time()) - 2 * one_day_second
    #     to_timestamp_str = datetime.datetime.fromtimestamp(from_timestamp - days * one_day_second).strftime(
    #         "%Y%m%d")
    #     from_timestamp_str = datetime.datetime.fromtimestamp(from_timestamp).strftime("%Y%m%d")
    #     return [str(date) for date in range(int(to_timestamp_str), int(from_timestamp_str))]
