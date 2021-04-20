from unittest import TestCase

from sqlalchemy import Table, MetaData, Column, String, text

from config.config_loader import load_yml_config
from config.mysql_config import MysqlConfig
from service.eland_member_mapping_service import ElandMemberMappingService


class TestElandMemberMappingService(TestCase):

    def get_instance(self):
        application_conf_file_path = './conf/application-test.yml'
        config = load_yml_config(application_conf_file_path, "eland")
        eland_member_mapping_service = ElandMemberMappingService(
            MysqlConfig.build(config['mysql']))
        return eland_member_mapping_service

    def create_table(self, service: ElandMemberMappingService):
        meta = MetaData()
        id_mapping = Table(
            'test_aggregate', meta,
            Column('uuid', String(255), index=True),
            Column('MemberID', String(255), index=True),
        )
        meta.create_all(service._engine)

    def del_table(self, service: ElandMemberMappingService):
        sql = text(
            "drop table test_aggregate")
        service.session().execute(sql)

    def insert(self, uuid, ctid, service: ElandMemberMappingService):
        sql = text(
            "insert into test_aggregate (uuid, MemberID) values ('{}','{}')".format(uuid, ctid))
        service.session().execute(sql)

    def test_find_all_ctid_by_uuid_empty(self):
        service = self.get_instance()
        self.create_table(service)

        result = service.find_all_ctid_by_uuid(['a'])

        self.assertEqual(result, [])

        self.del_table(service)

    def test_find_all_ctid_by_uuid_have_value_case1(self):
        service = self.get_instance()
        self.create_table(service)
        self.insert('a', '123', service)
        self.insert('a', '123', service)

        result = service.find_all_ctid_by_uuid(['a'])

        self.assertEqual(len(result), 1)
        self.del_table(service)

    def test_find_all_ctid_by_uuid_have_value_case2(self):
        service = self.get_instance()

        self.create_table(service)
        self.insert('a', '123', service)
        self.insert('b', '1234', service)

        result = service.find_all_ctid_by_uuid(['a', 'b'])
        print(result)
        self.assertEqual(len(result), 2)
        self.del_table(service)

    def test_find_all_ctid_by_uuid_empty_input(self):
        service = self.get_instance()
        self.create_table(service)

        result = service.find_all_ctid_by_uuid([])

        self.assertEqual(len(result), 0)
        self.del_table(service)
