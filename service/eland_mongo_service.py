from mongoengine import connect, get_db, QuerySet, Q
from mongoengine.pymongo_support import list_collection_names

from config.mongodb_config import MongoDBConfig
from document.eland_data_document import ElandDataDocument


class ElandDataMongoService:

    def __init__(self, config: MongoDBConfig):
        self._default_collection_name = config.collection_name
        self._connection = connect(db=config.database, host=config.host, port=config.port, username=config.username,
                                   password=config.password,
                                   authentication_source="admin")
        self._db = get_db()

    def find_all_by_query_only(self, collection_name=None, q: Q = None, *field):
        return self.__build_quert_set(collection_name).filter(q).all().only(*field)

    # TODO test
    def find_max_value_by_tag_name(self, collection_name=None, q: Q = None, order_by_tag_name=None, reverse=False):
        if reverse:
            order_by_tag_name = '-' + order_by_tag_name
        return self.__build_quert_set(collection_name).filter(q).order_by(order_by_tag_name).first()

    def __build_quert_set(self, collection_name=None):
        collection_name = self.__check_is_collection_name_is_none(collection_name)
        return QuerySet(ElandDataDocument,
                        ElandDataDocument().switch_collection(collection_name)._get_collection())

    def __check_is_collection_name_is_none(self, collection_name):
        return self._default_collection_name if collection_name is None else collection_name

    def list_collection_names(self):
        return list_collection_names(self._db)
