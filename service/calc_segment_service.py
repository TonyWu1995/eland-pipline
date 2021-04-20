import logging
from typing import (
    Dict,
    List,
    Any
)

import numpy as np

from constant.algo_type import AlgoType
from ml.algo.model import Model
from ml.algo.none_model import NoneModel
from ml.normalize import log_normalize

log = logging.getLogger(__name__)


class CalcSegmentService:

    def __init__(self, strategy_dict: Dict[AlgoType, Model]) -> None:
        self.__strategy_dict = strategy_dict

    # input array of [uuid,[score,max_value]]
    def calc(self, algo_type: str, value_list: List[Any]) -> List[str]:
        log.info("calc() age_type={} value_list size={}".format(algo_type, len(value_list)))
        normalize_value = np.array([log_normalize(value[1])[0] for value in value_list])
        value_list = list(zip([value[0] for value in value_list], normalize_value))
        threshold = self.get_model(algo_type).fit(normalize_value)
        result = self.__filter_less_than_threshold(threshold, value_list)
        log.info("calc() result size={}".format(len(result)))
        return result

    def __filter_less_than_threshold(self, threshold: float, value_list: List[Any]) -> List[str]:
        return [value[0] for value in value_list if value[1] >= threshold]

    def get_model(self, algo_type: str) -> Model:
        return self.__strategy_dict.get(AlgoType[algo_type.upper()], NoneModel())
