import logging

from algo.kmean_model import KmeanModel
from algo.none_model import NoneModel
from constant.algo_type import AlgoType

log = logging.getLogger(__name__)


class CalcSegmentService:
    strategy_dict = {
        AlgoType.KMEAN: KmeanModel(),
    }

    # TODO input strategy_dict
    def __init__(self, strategy_dict={}):
        pass

    # TODO input np one de array
    def calc(self, algo_type: str):
        log.debug("calc() age_type={}".format(algo_type))
        model = self.strategy_dict.get(AlgoType[algo_type.upper()], NoneModel())
        # model.fit()
        pass
