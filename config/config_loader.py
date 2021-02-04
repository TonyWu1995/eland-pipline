import yaml

def load_config(file_path: str, dict_key: str):
    with open(file_path, 'r') as stream:
        data = yaml.safe_load(stream)
    return data[dict_key]
