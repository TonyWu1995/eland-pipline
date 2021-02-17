import logging

from constant.algo_type import AlgoType
from ml.algo.none_model import NoneModel
from ml.normalize import log_normalize
import numpy as np
log = logging.getLogger(__name__)


class CalcSegmentService:

    def __init__(self, strategy_dict):
        self.__strategy_dict = strategy_dict

    # input array of uuid,[score,max_value]
    def calc(self, algo_type: str, value_list):
        log.debug("calc() age_type={} value_list size={}".format(algo_type, len(value_list)))
        print(value_list)
        normalize_value = np.array([log_normalize(value[1])[0] for value in value_list])
        value_list = list(zip([value[0] for value in value_list], normalize_value))
        threshold = self.get_model(algo_type).fit(normalize_value)
        return self.__filter_less_than_threshold(threshold, value_list)

    def __filter_less_than_threshold(self, threshold, value_list):
        return [value[0] for value in value_list if value[1] >= threshold]

    def get_model(self, algo_type: str):
        return self.__strategy_dict.get(AlgoType[algo_type.upper()], NoneModel())
