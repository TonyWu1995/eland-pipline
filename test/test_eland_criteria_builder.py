from unittest import TestCase

from constant.age import Age
from constant.gender import Gender
from service.eland_criteria_builder import query_build


class TestElandCriteriaBuilder(TestCase):

    def test_build_success_case1(self):
        self.assertEqual(query_build("age_tag", 'EIGHTEEN_TWENTY_FOUR', 123, 456),
                         {'age_tag': Age.EIGHTEEN_TWENTY_FOUR, 'update_at__gte': 123, 'update_at__lt': 456}
                         )

    def test_build_success_case2(self):
        self.assertEqual(query_build("gender_tag", 'EIGHTEEN_TWENTY_FOUR', 123, 456),
                         {'gender_tag': 'EIGHTEEN_TWENTY_FOUR', 'update_at__gte': 123, 'update_at__lt': 456}
                         )

    def test_build_success_case3(self):
        self.assertEqual(query_build("gender_tag", 'FEMALE', 123, 456),
                         {'gender_tag': Gender.FEMALE, 'update_at__gte': 123, 'update_at__lt': 456}
                         )

    def test_build_success_case4(self):
        self.assertEqual(query_build("interest.tag", '性別:男性', 123, 456),
                         {'interest.tag': "性別:男性", 'update_at__gte': 123, 'update_at__lt': 456}
                         )
