from unittest import TestCase

from constant.algo_type import AlgoType
from ml.algo.kmean_model import KmeanModel
from ml.calc_ml_service import CalcMLService


class TestCalcSegmentService(TestCase):

    def test_get_model_kmean(self):
        kmean = KmeanModel()
        service = CalcMLService(strategy_dict={
            AlgoType.KMEAN: kmean,
        })
        model = service.get_model("kmean")
        self.assertEqual(model, kmean)
