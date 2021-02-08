from mongoengine import Q

from constant.age import Age
from constant.gender import Gender
from constant.geo import Geo
from constant.income import Income
from document.eland_data_document import ElandDataDocument


class ElandCriteriaBuilder:
    eland_data_dict = {
        ElandDataDocument.gender_tag.name: Gender.__members__,
        ElandDataDocument.income_tag.name: Income.__members__,
        ElandDataDocument.age_tag.name: Age.__members__,
        ElandDataDocument.geo_tag.name: Geo.__members__,
    }

    def __init__(self):
        pass

    def build(self, criteria_key, criteria_value, from_timestamp, to_timestamp):
        #  {'age_tag': Gender.FEMALE, 'update_at__gte': 124, 'update_at__lt': 457}
        update_at = ElandDataDocument.update_at.name
        return {
            criteria_key: self._get_criteria_value(criteria_key, criteria_value),
            update_at + "__gte": from_timestamp,
            update_at + "__lt": to_timestamp
        }

    def __build_update_at_criteria(self, from_timestamp, to_timestamp):
        update_at = ElandDataDocument.update_at.name
        return Q(**{update_at + "__gte": from_timestamp}) & Q(**{update_at + "__lt": to_timestamp})

    def _get_criteria_value(self, criteria_key, criteria_value):
        criteria_dict = self.eland_data_dict.get(criteria_key, {})
        return criteria_dict.get(criteria_value.upper(), criteria_value)
