from typing import (
    Any,
    List
)

from sklearn.cluster import KMeans

from ml.algo.model import Model


class KmeanModel(Model):

    def __init__(self) -> None:
        super().__init__()

    def fit(self, data_value: List[Any]) -> float:
        km = KMeans(n_clusters=3, random_state=0, max_iter=300)
        km.fit(data_value.reshape(-1, 1))
        threshold = list(km.cluster_centers_)
        threshold.sort()
        return threshold[0]
