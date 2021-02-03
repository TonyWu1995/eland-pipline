import pymongo


class ElandMongoRepo:
    # TODO mongo config
    def __init__(self):
        self.client = pymongo.MongoClient(host="192.168.101.41", port=27017, username="admin", password="admin")
        self.db = self.client['eland_data']

    def find_all(self, collections: str, query1=None, query2=None):
        if query2 is None:
            return self.db[collections].find(query1)
        else:
            return self.db[collections].find(query1, query2)

    def count(self, collections: str, query1=None, query2=None):
        return self.find_all(collections, query1, query2).count()


