# from mongoengine import Q
import numpy as np
from sklearn.cluster import KMeans

x = np.random.random(13876)

print(x)
# print(x.reshape(-1, 1))
km = KMeans(n_clusters=3, random_state=0, max_iter=300)
km.fit(x.reshape(-1,1))  # -1 will be calculated to be 13876 here
threshold = km.cluster_centers_
print(threshold)
# from itertools import zip_longest
#
# a = [1, 2, 3]
# b = []
# zipped = zip_longest(a, b)
# print(list(zipped))
# Q
# from mongoengine import Q
#
# c = None
# for row in ['302df362ef5d4f5595a3186fa7b32a20021815', '30135a91d68e4fe790c07ea1fa094edb091919']:
#     flt = {'uuid': row}
#     if c is None:
#         c = Q(**flt)
#     else:
#         c |= Q(**flt)
# print(c)

# switch colections
# QuerySet(ElandData, ElandData().switch_collection("test")._get_collection())

# gt le...
# condition = {'interest__tag_gt': '性別:男性'}
# t = Q(interest__score__lt=float(1))
# print(t)
# old_objects = QuerySet(ElandData, ElandData._get_collection())
# for row in old_objects.all().filter(t).limit(10):
#     print(row.uuid)
#     for j in row.interest:
#         print(j.tag, j.score)
