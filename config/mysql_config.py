from typing import (
    Dict,
    Any
)


class MysqlConfig:

    def __init__(self, url: str, table_name: str):
        self.__url = url
        self.__table_name = table_name

    @property
    def url(self) -> str:
        return self.__url

    @property
    def table_name(self) -> str:
        return self.__table_name

    @staticmethod
    def build(config: Dict[str, Any]) -> Any:
        return MysqlConfig(config['url'],
                           config['table-name'])
