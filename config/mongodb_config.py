from typing import (
    Dict,
    Any
)


class MongoDBConfig:

    def __init__(self, host: str,
                 port: int,
                 database: str,
                 username: str,
                 password: str,
                 collection_name: str,
                 cursor_batch_size: int):
        self.__host = host
        self.__port = port
        self.__database = database
        self.__username = username
        self.__password = password
        self.__collection_name = collection_name
        self.__cursor_batch_size = cursor_batch_size

    @property
    def host(self) -> str:
        return self.__host

    @property
    def port(self) -> int:
        return self.__port

    @property
    def database(self) -> str:
        return self.__database

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @property
    def collection_name(self) -> str:
        return self.__collection_name

    @property
    def cursor_batch_size(self) -> str:
        return self.__cursor_batch_size

    @staticmethod
    def build(config: Dict[str, Any]) -> Any:
        return MongoDBConfig(config['host'],
                             config['port'],
                             config['database'],
                             config['username'],
                             config['password'],
                             config['collection-name'],
                             config['cursor-batch-size'])
