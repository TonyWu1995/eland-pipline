import json
from typing import (
    Dict,
    Any
)

import yaml


def load_yml_config(file_path: str, dict_key: str) -> Dict[str, Any]:
    with open(file_path, 'r') as stream:
        data = yaml.safe_load(stream)
    return data[dict_key]


def load_json_config(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r', encoding="utf-8") as stream:
        return json.load(stream)
