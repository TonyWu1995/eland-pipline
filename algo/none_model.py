from algo.model import Model


class NoneModel(Model):

    def __init__(self):
        pass

    def fit(self, data_list):
        return -1
