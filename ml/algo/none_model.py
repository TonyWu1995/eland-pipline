from typing import (
    Any,
    List
)

from ml.algo.model import Model


class NoneModel(Model):

    def __init__(self):
        pass

    def fit(self, data_list: List[Any]):
        return -1
