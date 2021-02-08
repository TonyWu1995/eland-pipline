import logging

from constant.algo_type import AlgoType
from ml.algo.none_model import NoneModel

log = logging.getLogger(__name__)


class CalcSegmentService:

    def __init__(self, strategy_dict={}):
        self.__strategy_dict = strategy_dict

    # TODO input np one de array
    def calc(self, algo_type: str):
        log.debug("calc() age_type={}".format(algo_type))

        # model.fit()
        pass

    def get_model(self, algo_type: str):
        return self.__strategy_dict.get(AlgoType[algo_type.upper()], NoneModel())
