from unittest import TestCase

from constant.algo_type import AlgoType
from ml.algo.kmean_model import KmeanModel
from ml.calc_ml_service import CalcSegmentService


class TestCalcMLService(TestCase):

    def test_get_model_kmean(self):
        kmean = KmeanModel()
        service = CalcSegmentService(strategy_dict={
            AlgoType.KMEAN: kmean,
        })
        model = service.get_model("kmean")
        self.assertEqual(model, kmean)
