from unittest import TestCase

from constant.algo_type import AlgoType
from ml.algo.kmean_model import KmeanModel
from ml.algo.model import Model
from service.calc_segment_service import CalcSegmentService


class TestCalcMLService(TestCase):

    def test_get_model_kmean(self):
        kmean = KmeanModel()
        service = CalcSegmentService(strategy_dict={
            AlgoType.KMEAN: kmean,
        })
        model = service.get_model("kmean")
        self.assertEqual(model, kmean)

    def test_calc_none_model_case1(self):
        service = CalcSegmentService(strategy_dict={})
        result = service.calc("none", [['1', 123]])
        self.assertEqual(result, ['1'])

    def test_calc_none_model_case2(self):
        service = CalcSegmentService(strategy_dict={})
        result = service.calc("none", [['1', 123], ['2', 123]])
        self.assertEqual(result, ['1', '2'])

    def test_calc_kmean_model_case1(self):
        service = CalcSegmentService(strategy_dict={
            AlgoType.KMEAN: FakeKmeanModel(),
        })
        result = service.calc("kmean", [['1', 123], ['2', 123]])
        self.assertEqual(result, ['1', '2'])

    def test_calc_kmean_model_case2(self):
        service = CalcSegmentService(strategy_dict={
            AlgoType.KMEAN: FakeKmeanModel(),
        })
        result = service.calc("kmean", [['1', 99], ['2', 123]])
        print(result)
        self.assertEqual(result, ['2'])


class FakeKmeanModel(Model):

    def __init__(self):
        pass

    def fit(self, data_value):
        return 1
