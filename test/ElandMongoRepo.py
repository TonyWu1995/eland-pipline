from mongoengine import connect, get_db

# c = connect(db='eland_data', host='192.168.101.41', port=27017, username="admin", password="admin",
#             authentication_source="admin")
#
# print(list_collection_names(get_db()))
from mongoengine.pymongo_support import list_collection_names


class ElandMongoRepo:

    def __init__(self):
        self._connection = connect(db='eland_data', host='192.168.101.41', port=27017, username="admin",
                                   password="admin",
                                   authentication_source="admin")

        self._db = get_db()



    def list_collection_names(self):
        return list_collection_names(self._db)


repo = ElandMongoRepo()

print(repo.list_collection_names())
