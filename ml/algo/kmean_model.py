from sklearn.cluster import KMeans

from ml.algo.model import Model


class KmeanModel(Model):

    def __init__(self):
        super().__init__()

    def fit(self, data_value):
        km = KMeans(n_clusters=3, random_state=0, max_iter=300)
        km.fit([[float(i)] for i in data_value])
        threshold = km.cluster_centers_
        # TODO filter
        return None
