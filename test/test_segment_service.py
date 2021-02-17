from unittest import TestCase

# TODO
from mongoengine import Q

from config.segment_config import SegmentConfig
from document.eland_data_document import ElandDataDocument, InterestDocument
from service.calc_segment_service import CalcSegmentService
from service.eland_criteria_builder import ElandCriteriaBuilder
from service.eland_member_mapping_service import ElandMemberMappingService
from service.eland_mongo_service import ElandDataMongoService
from service.generate_segment_service import GenerateSegmentService


class FakeEmptyElandDataMongoService(ElandDataMongoService):

    def __init__(self):
        pass

    def find_all_by_query_only(self, collection_name=None, q: Q = None, *field):
        return [ElandDataDocument(
            uuid='a',
        )]


class FakeElandDataMongoService(ElandDataMongoService):

    def __init__(self):
        pass

    def find_all_by_query_only(self, collection_name=None, q: Q = None, *field):
        return [ElandDataDocument(
            uuid='a',
            interest=[
                InterestDocument(
                    tag="族群:健身族",
                    score=100
                )
            ]
        ), ElandDataDocument(
            uuid='b',
            interest=[
                InterestDocument(
                    tag="族群:健身族",
                    score=101
                )
            ]
        ), ElandDataDocument(
            uuid='c',
            interest=[
                InterestDocument(
                    tag="族群:健身族",
                    score=102
                )
            ]
        )]


class FakeEmptyElandMemberMappingService(ElandMemberMappingService):
    dict = {
        'a': ['1', '2', '3'],
        'b': ['4'],
        'c': ['5']
    }

    def __init__(self):
        pass

    def find_all_ctid_by_uuid(self, uuid_list):
        result_list = []
        for row in uuid_list:
            result_list = result_list + self.dict[row]
        return result_list


class TestGenerateSegmentService(TestCase):

    def get_empty_instance(self):
        stub_eland_data_mongo_service = FakeEmptyElandDataMongoService()
        stub_eland_member_mapping_service = FakeEmptyElandMemberMappingService()
        generate_segment_service = GenerateSegmentService(stub_eland_data_mongo_service,
                                                          stub_eland_member_mapping_service,
                                                          ElandCriteriaBuilder(), CalcSegmentService({}))
        return generate_segment_service

    def get_instance(self):
        stub_eland_data_mongo_service = FakeElandDataMongoService()
        stub_eland_member_mapping_service = FakeEmptyElandMemberMappingService()
        generate_segment_service = GenerateSegmentService(stub_eland_data_mongo_service,
                                                          stub_eland_member_mapping_service,
                                                          ElandCriteriaBuilder(), CalcSegmentService({}))
        return generate_segment_service

    def test_generate_empty(self):
        generate_segment_service = self.get_empty_instance()
        config = SegmentConfig(
            criteria_key="gender_tag",
            criteria_value="FEMALE",
            algo="None",
            day=30,
            export_file_name="test_seg_tags_eland_female_{}_ctid_c{}"
        )
        ctid_list = generate_segment_service.generate(config)

        self.assertEqual(ctid_list, ['1', '2', '3'])

    def test_generate(self):
        generate_segment_service = self.get_instance()
        config = SegmentConfig(
            criteria_key="interest__tag",
            criteria_value="族群:健身族",
            algo="kmean",
            day=30,
            export_file_name="test_seg_tags_eland_female_{}_ctid_c{}"
        )
        ctid_list = generate_segment_service.generate(config)
        print(ctid_list)
        self.assertEqual(ctid_list, ['1', '2', '3', '4', '5'])

    def test_query_eland_data_empty(self):
        generate_segment_service = self.get_empty_instance()
        config = SegmentConfig(
            criteria_key="gender_tag",
            criteria_value="FEMALE",
            algo="None",
            day=30,
            export_file_name="test_seg_tags_eland_female_{}_ctid_c{}"
        )
        result = generate_segment_service._query_eland_data(30, config.criteria_key, config.criteria_value)

        self.assertEqual(result, [('a', [0, 0])])

    def test_query_eland_data(self):
        generate_segment_service = self.get_instance()
        config = SegmentConfig(
            criteria_key="interest__tag",
            criteria_value="族群:健身族",
            algo="kmean",
            day=30,
            export_file_name="test_seg_tags_eland_female_{}_ctid_c{}"
        )
        result = generate_segment_service._query_eland_data(30, config.criteria_key, config.criteria_value)

        expect = [('a', [100.0, 100.0]), ('b', [101.0, 101.0]), ('c', [102.0, 102.0])]
        self.assertEqual(result, expect)
