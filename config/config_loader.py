import json

import yaml


def load_yml_config(file_path: str, dict_key: str):
    with open(file_path, 'r') as stream:
        data = yaml.safe_load(stream)
    return data[dict_key]


def load_json_config(file_path):
    with open(file_path, 'r',encoding="utf-8") as stream:
        return json.load(stream)
