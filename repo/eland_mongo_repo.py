from mongoengine import connect, get_db, QuerySet, Q
from mongoengine.pymongo_support import list_collection_names

from config.mongodb_config import MongoDBConfig
from document.eland_data_document import ElandDataDocument


class ElandDataMongoRepo:

    def __init__(self, config: MongoDBConfig):
        self._connection = connect(db=config.database, host=config.host, port=config.port, username=config.username,
                                   password=config.password,
                                   authentication_source="admin")
        self._db = get_db()

    def find_all_by_query(self, collection_name, q: Q):
        query_set = QuerySet(ElandDataDocument,
                             ElandDataDocument().switch_collection(collection_name)._get_collection())
        return query_set.filter(q).all()

    def find_all_by_query_only(self, collection_name, q: Q, *field):
        return self.find_all_by_query(collection_name, q).only(*field)

    def list_collection_names(self):
        return list_collection_names(self._db)
