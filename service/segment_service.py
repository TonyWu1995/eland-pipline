import logging
import time

import numpy as np
from mongoengine import Q

from ml.calc_ml_service import CalcMLService
from service.eland_criteria_builder import ElandCriteriaBuilder
from service.eland_mongo_service import ElandDataMongoService

log = logging.getLogger(__name__)


class GenerateSegmentService:

    # TODO mysql connector
    def __init__(self,
                 mongo_repo: ElandDataMongoService,
                 builder: ElandCriteriaBuilder,
                 calc_ml_service: CalcMLService):
        self.__mongo_repo = mongo_repo
        self.__eland_criteria_builder = builder
        self.__calc_ml_service = calc_ml_service

    def generate(self, config):
        log.debug("generate() config={}".format(config))
        # TODO config obj
        query_result_list = self.__query(config['day'], config['criteria_key'], config['criteria_value'])
        threshold = self.__calc_ml_service.calc(config['algo'],
                                                np.array([float(result[1]) for result in
                                                          self.__query_result(query_result_list)]))
        # TODO filter and get mysql ctid
        pass

    def __query(self, day, criteria_key, criteria_value):
        from_timestamp, to_timestamp = self.__calc_from_timestamp_and_to_timestamp(day)
        criteria_query = self.__eland_criteria_builder.query_build(criteria_key,
                                                                   criteria_value,
                                                                   from_timestamp,
                                                                   to_timestamp)
        criteria_only = self.__eland_criteria_builder.only_build(criteria_key)
        return self.__mongo_repo.find_all_by_query_only("test_aggregate",
                                                        Q(**criteria_query),
                                                        *criteria_only)

    # if new data format and extract it to obj
    def __query_result(self, query_list):
        result_list = []
        for eland_data_doc in query_list:
            score = 0
            if len(eland_data_doc.interest) > 0:
                score = [interest.score for interest in eland_data_doc.interest][0]
            result = [eland_data_doc.uuid, score]
            result_list.append(result)
        return result_list

    def __calc_from_timestamp_and_to_timestamp(self, days):
        one_day_second = 86400
        to_timestamp = int(time.time()) - 2 * one_day_second
        from_timestamp = to_timestamp - one_day_second * days
        return from_timestamp, to_timestamp
