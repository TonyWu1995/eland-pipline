import math


def log_normalize(value_list):
    max_value = max(value_list)
    if max_value == 0 or value_list[0] == 0:
        return value_list
    try:
        return [math.log10(value) / math.log10(max_value) for value in value_list]
    except Exception as e:
        return [0, 0]
