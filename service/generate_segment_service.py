import logging
import time

from mongoengine import Q

from config.segment_config import SegmentConfig
from service.calc_segment_service import CalcSegmentService
from service.eland_criteria_builder import ElandCriteriaBuilder
from service.eland_member_mapping_service import ElandMemberMappingService
from service.eland_mongo_service import ElandDataMongoService

log = logging.getLogger(__name__)


class GenerateSegmentService:

    def __init__(self,
                 mongo_repo: ElandDataMongoService,
                 eland_member_mapping_service: ElandMemberMappingService,
                 builder: ElandCriteriaBuilder,
                 calc_ml_service: CalcSegmentService):
        self.__mongo_repo = mongo_repo
        self.__member_mapping_service = eland_member_mapping_service
        self.__eland_criteria_builder = builder
        self.__calc_ml_service = calc_ml_service

    def generate(self, config: SegmentConfig):
        log.debug("generate() config={}".format(config))
        query_mongodb_result_list = self._query_eland_data(config.day, config.criteria_key,
                                                            config.criteria_value)
        ctid_list = self.__member_mapping_service.find_all_ctid_by_uuid(self.__calc_ml_service.calc(config.algo,
                                                                                                    query_mongodb_result_list))
        log.info("generate() ctid size={}".format(len(ctid_list)))
        return ctid_list

    def _query_eland_data(self, day, criteria_key, criteria_value):
        log.info("__query() day={}, key={}, value={}".format(day, criteria_key, criteria_value))
        from_timestamp, to_timestamp = self.__calc_from_timestamp_and_to_timestamp(day)
        q = Q(**self.__eland_criteria_builder.query_build(criteria_key,
                                                          criteria_value,
                                                          from_timestamp,
                                                          to_timestamp))
        criteria_only = self.__eland_criteria_builder.only_build(criteria_key)
        query_list = self.__mongo_repo.find_all_by_query_only(None,
                                                              q,
                                                              *criteria_only)
        uuid_list = [eland_data_doc.uuid for eland_data_doc in query_list]
        score_list = []
        for eland_data_doc in query_list:
            if len(eland_data_doc.interest) > 0:
                for interest in eland_data_doc.interest:
                    if interest.tag == criteria_value:
                        score_list.append(
                            [float(interest.score), max(eland_data_doc.interest, key=lambda item: item['score']).score])
            else:
                score_list.append([0, 0])
        return list(zip(uuid_list, score_list))

    def __calc_from_timestamp_and_to_timestamp(self, days):
        one_day_second = 86400
        to_timestamp = int(time.time()) - 2 * one_day_second
        from_timestamp = to_timestamp - one_day_second * days
        return from_timestamp, to_timestamp
