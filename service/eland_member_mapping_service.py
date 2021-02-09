import logging

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from config.mysql_config import MysqlConfig

log = logging.getLogger(__name__)


class ElandMemberMappingService:

    # TODO mysql config
    def __init__(self, config: MysqlConfig):
        self.__default_table_name = config.table_name
        connection_url = "mysql+pymysql://{}:{}@{}:{}/{}".format(config.username, config.password, config.host,
                                                                 config.port, config.database)
        engine = create_engine(connection_url)
        engine.connect()
        self.session = sessionmaker(bind=engine)()

    def find_all_ctid_by_uuid(self, uuid_list):
        log.debug("find_all_ctid_by_uuid() uuid_list size={}", len(uuid_list))
        if len(uuid_list) == 1:
            sql = text(
                "select distinct(ctid) from {} where uuid = {} group by uuid,ctid".format(self.__default_table_name,
                                                                                          uuid_list[0]))
        else:
            sql = text(
                "select distinct(ctid) from {} where uuid in {} group by uuid,ctid".format(
                    self.__default_table_name,
                    tuple(uuid_list)))

        return [row[0] for row in self.session.execute(sql)]
