from sklearn.cluster import KMeans

from ml.algo.model import Model


class KmeanModel(Model):

    def __init__(self):
        super().__init__()

    # TODO check if cerjary get correct threshold
    def fit(self, data_value):
        km = KMeans(n_clusters=3, random_state=0, max_iter=300)
        km.fit(data_value.reshape(-1, 1))
        threshold = km.cluster_centers_
        return threshold[1]
