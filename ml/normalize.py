import math

import numpy as np


def log_normalize(value_list):
    max_value = max(value_list)
    if max_value == 0:
        return value_list
    return np.array([math.log10(value) / math.log10(max_value) for value in value_list])
