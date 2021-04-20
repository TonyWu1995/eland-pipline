import logging
from typing import List

from sqlalchemy import (
    create_engine
)
from sqlalchemy.orm import sessionmaker

from config.mysql_config import MysqlConfig

log = logging.getLogger(__name__)


class ElandMemberMappingService:

    def __init__(self, config: MysqlConfig) -> None:
        self.__default_table_name = config.table_name
        self._engine = create_engine(config.url, pool_size=20, pool_pre_ping=True)
        self._engine.connect()
        self.session = sessionmaker(bind=self._engine)

    def __execute(self, sql: str) -> List[str]:
        log.info("__execute start")
        try:
            session = self.session()
            result = [row[0] for row in session.execute(sql)]
            session.close()
            return result
        except Exception as e:
            log.error(e)
            return []

    def find_all_ctid_by_uuid(self, uuid_list: List[str] = []) -> List[str]:
        log.info("find_all_ctid_by_uuid() uuid_list size={}".format(len(uuid_list)))
        if len(uuid_list) == 0:
            return []
        batch_value = 50000
        times = int(len(uuid_list) / batch_value) if len(uuid_list) % batch_value == 0 else int(
            len(uuid_list) / batch_value) + 1
        sql_list = []
        for time in range(0, times):
            query_list = uuid_list[time * batch_value:time * batch_value + batch_value]
            if len(query_list) == 1:
                sql = "select MemberID from {} where uuid = '{}' group by UUID,MemberID".format(
                    self.__default_table_name,
                    query_list[0]
                )
            else:
                sql = "select MemberID from {} where uuid in {} group by UUID,MemberID".format(
                    self.__default_table_name,
                    tuple(query_list))
            sql_list.append(sql)
        result = [self.__execute(sql) for sql in sql_list]
        log.info("find_all_ctid_by_uuid() result size={}".format(len(result)))
        return list(set([ctid for ctid_list in result for ctid in ctid_list]))
