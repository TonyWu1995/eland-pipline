from typing import (
    Dict,
    Any, List
)


class SegmentConfig:

    def __init__(self, criteria_key: str, criteria_value: Any, algo: str, day: int, export_file_name: str):
        self.__criteria_key = criteria_key
        self.__criteria_value = criteria_value
        self.__algo = algo
        self.__day = day
        self.__export_file_name = export_file_name

    @property
    def criteria_key(self) -> str:
        return self.__criteria_key

    @property
    def criteria_value(self) -> Any:
        return self.__criteria_value

    @property
    def algo(self) -> str:
        return self.__algo

    @property
    def day(self) -> int:
        return self.__day

    @property
    def export_file_name(self) -> str:
        return self.__export_file_name

    @staticmethod
    def build(config: Dict[str, Any]) -> Any:
        return SegmentConfig(config['criteria_key'], config['criteria_value'], config['algo'], config['day'],
                             config['export_file_name'])

    @staticmethod
    def build_list(config_list: List[Any]) -> Any:
        return [SegmentConfig.build(config) for config in config_list]
