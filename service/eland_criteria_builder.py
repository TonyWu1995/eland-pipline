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
        update_at = ElandDataDocument.update_at.name
        return {criteria_key: self.get_criteria_value(criteria_key, criteria_value),
                update_at + "_gte": from_timestamp,
                update_at + "_le": to_timestamp}

    def get_criteria_value(self, criteria_key, criteria_value):
        criteria_dict = self.eland_data_dict.get(criteria_key, {})
        return criteria_dict.get(criteria_value.upper(), criteria_value)
