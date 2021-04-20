import gc
import logging
import time
from typing import (
    List,
    Tuple
)

from config.segment_config import SegmentConfig
from service.calc_segment_service import CalcSegmentService
from service.eland_member_mapping_service import ElandMemberMappingService
from service.eland_mongo_service import ElandDataMongoService

log = logging.getLogger(__name__)


class GenerateSegmentService:

    def __init__(self,
                 mongo_repo: ElandDataMongoService,
                 eland_member_mapping_service: ElandMemberMappingService,
                 calc_ml_service: CalcSegmentService):
        self.__mongo_repo = mongo_repo
        self.__member_mapping_service = eland_member_mapping_service
        self.__calc_ml_service = calc_ml_service

    def generate(self, config: SegmentConfig) -> List[str]:
        log.debug("generate() config={}".format(config))
        from_timestamp, to_timestamp = self.__calc_from_timestamp_and_to_timestamp(config.day)
        query_mongodb_result_list = self.__mongo_repo.find_all_batch(None,
                                                                     config.criteria_key,
                                                                     config.criteria_value,
                                                                     from_timestamp,
                                                                     to_timestamp)
        ctid_list = self.__member_mapping_service.find_all_ctid_by_uuid(self.__calc_ml_service.calc(config.algo,
                                                                                                    query_mongodb_result_list)
                                                                        )
        del query_mongodb_result_list
        gc.collect()
        log.info("generate() ctid size={}".format(len(ctid_list)))
        return ctid_list

    def __calc_from_timestamp_and_to_timestamp(self, days: int) -> Tuple[int, int]:
        one_day_second = 86400
        to_timestamp = int(time.time())
        from_timestamp = to_timestamp - one_day_second * days
        return from_timestamp, to_timestamp
