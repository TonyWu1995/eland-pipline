import logging

from constant.algo_type import AlgoType
from ml.algo.none_model import NoneModel

log = logging.getLogger(__name__)


class CalcMLService:

    def __init__(self, strategy_dict={}):
        self.__strategy_dict = strategy_dict

    def calc(self, algo_type: str, value_list):
        log.debug("calc() age_type={}".format(algo_type))
        return self.get_model(algo_type).fit(value_list)

    def get_model(self, algo_type: str):
        return self.__strategy_dict.get(AlgoType[algo_type.upper()], NoneModel())
