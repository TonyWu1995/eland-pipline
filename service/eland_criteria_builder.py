from typing import (
    Dict,
    Any
)

from constant.age import Age
from constant.gender import Gender
from constant.geo import Geo
from constant.income import Income
from document.eland_data_document import ElandDataDocument

eland_data_dict = {
    ElandDataDocument.gender_tag.name: Gender.__members__,
    ElandDataDocument.income_tag.name: Income.__members__,
    ElandDataDocument.age_tag.name: Age.__members__,
    ElandDataDocument.geo_tag.name: Geo.__members__,
}


def only_build(criteria_key: str) -> Dict[str, int]:
    result = {"uuid": 1}
    if criteria_key == "interest__tag":
        result['interest.tag'] = 1
        result['interest.score'] = 1
    return result


def query_build(criteria_key: str,
                criteria_value: str,
                from_timestamp: int,
                to_timestamp: int) -> Dict[str, Any]:
    if type(criteria_value) is str:
        criteria_value = criteria_value.upper()
    criteria_value = eland_data_dict.get(criteria_key, {}).get(criteria_value, criteria_value)
    update_at = ElandDataDocument.update_at.name
    return {
        criteria_key: criteria_value,
        update_at + "__gte": from_timestamp,
        update_at + "__lt": to_timestamp
    }
