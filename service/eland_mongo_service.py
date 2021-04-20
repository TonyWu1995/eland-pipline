import gc
import logging
from typing import (
    List,
    Dict, Any
)

from mongoengine import (
    connect,
    get_db,
    QuerySet,
    Q
)
from mongoengine.pymongo_support import list_collection_names

from config.mongodb_config import MongoDBConfig
from document.eland_data_document import ElandDataDocument
from service.eland_criteria_builder import query_build, only_build

log = logging.getLogger(__name__)


class ElandDataMongoService:

    def __init__(self, config: MongoDBConfig) -> None:
        self._default_collection_name = config.collection_name
        self._connection = connect(db=config.database, host=config.host, port=config.port, username=config.username,
                                   password=config.password,
                                   authentication_source="admin")
        self._db = get_db()
        self._batch_size = config.cursor_batch_size

    def find_all_batch(self, collection_name: str = None,
                       criteria_key: str = None,
                       criteria_value: str = None,
                       from_timestamp: int = 0,
                       to_timestamp: int = 0) -> List[Any]:
        log.info("find_all_batch() collection_name={} criteria_key={} criteria_value={}".format(collection_name,
                                                                                                criteria_key,
                                                                                                criteria_value))

        q = Q(**query_build(criteria_key,
                            criteria_value,
                            from_timestamp,
                            to_timestamp))
        sql = QuerySet(ElandDataDocument, ElandDataDocument()._get_collection()) \
            .filter(q) \
            .all() \
            ._query

        only_field = only_build(criteria_key)
        collection_name = self.__check_is_collection_name_is_none(collection_name)
        count = self.__count(collection_name, sql, only_field)
        log.info("find_all_batch() count={}".format(count))
        result_list = []
        for c in range(0, count, self._batch_size):
            log.info("find_all_batch() batch start")
            try:
                cursor = self._db[collection_name].find(sql, only_field).skip(c).limit(self._batch_size)
                cursor.batch_size(self._batch_size)
                result_list.append(self.__format_eland_data_doc(list(cursor), criteria_value))
            except Exception as e:
                log.error("find_all_batch() error={}".format(e))
        # TODO
        result = [c for cursor in result_list for c in cursor]
        log.info("find_all_batch() result size={}".format(len(result)))
        return result

    def __format_eland_data_doc(self, eland_data_doc_list: List[Any], criteria_value: str) -> List[Any]:
        log.info("__format_eland_data_doc() size={}".format(len(eland_data_doc_list)))
        result = []
        for eland_data_doc in eland_data_doc_list:
            if 'interest' in eland_data_doc:
                max_value = max(eland_data_doc['interest'], key=lambda item: item['score'])['score']
                for interest in eland_data_doc['interest']:
                    if interest['tag'] == criteria_value:
                        result.append(
                            (eland_data_doc['uuid'], [float(interest['score']), max_value]))
            else:
                result.append((eland_data_doc['uuid'], [0, 0]))
        del eland_data_doc_list
        gc.collect()
        return result

    def __count(self, collection_name, sql, field: Dict[str, int] = None) -> int:
        return self._db[collection_name].find(sql, field).count()

    def __check_is_collection_name_is_none(self, collection_name: str) -> str:
        return self._default_collection_name if collection_name is None else collection_name

    def list_collection_names(self) -> List[str]:
        return list_collection_names(self._db)
