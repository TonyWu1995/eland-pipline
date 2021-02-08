from unittest import TestCase

from constant.age import Age
from constant.gender import Gender
from service.eland_criteria_builder import ElandCriteriaBuilder


class TestElandCriteriaBuilder(TestCase):

    def test_get_criteria_key_success_get_case1(self):
        builder = ElandCriteriaBuilder()
        self.assertEqual(builder._get_criteria_value("gender_tag", 'female'), Gender.FEMALE)

    def test_get_criteria_key_success_get_case2(self):
        builder = ElandCriteriaBuilder()
        self.assertEqual(builder._get_criteria_value("gender_tag", 'FEMALE'), Gender.FEMALE)

    def test_get_criteria_key_unknown_get(self):
        builder = ElandCriteriaBuilder()
        self.assertEqual(builder._get_criteria_value("gender_tag", '0'), '0')

    def test_build_success_case1(self):
        builder = ElandCriteriaBuilder()
        self.assertEqual(builder.build("age_tag", 'EIGHTEEN_TWENTY_FOUR', 123, 456),
                         {'age_tag': Age.EIGHTEEN_TWENTY_FOUR, 'update_at__gte': 123, 'update_at__lt': 456}
                         )

    def test_build_success_case2(self):
        builder = ElandCriteriaBuilder()
        self.assertEqual(builder.build("gender_tag", 'EIGHTEEN_TWENTY_FOUR', 123, 456),
                         {'gender_tag': 'EIGHTEEN_TWENTY_FOUR', 'update_at__gte': 123, 'update_at__lt': 456}
                         )

    def test_build_success_case3(self):
        builder = ElandCriteriaBuilder()
        self.assertEqual(builder.build("gender_tag", 'FEMALE', 123, 456),
                         {'gender_tag': Gender.FEMALE, 'update_at__gte': 123, 'update_at__lt': 456}
                         )

    def test_build_success_case4(self):
        builder = ElandCriteriaBuilder()
        self.assertEqual(builder.build("interest.tag", '性別:男性', 123, 456),
                         {'interest.tag': "性別:男性", 'update_at__gte': 123, 'update_at__lt': 456}
                         )