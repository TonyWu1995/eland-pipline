import time
from unittest import TestCase

from mongoengine import QuerySet

from config.config_loader import load_yml_config
from config.mongodb_config import MongoDBConfig
from constant.age import Age
from constant.gender import Gender
from constant.geo import Geo
from constant.income import Income
from document.eland_data_document import LocationDocument, ElandDataDocument, HabitWeekDayDocument, HabitHourDocument, \
    InterestDocument
from service.eland_mongo_service import ElandDataMongoService


class TestElandDataMongoService(TestCase):

    def get_instance(self):
        application_conf_file_path = './conf/application-test.yml'
        config = load_yml_config(application_conf_file_path, "eland")
        eland_data_mongo_service = ElandDataMongoService(
            MongoDBConfig.build(config['mongodb']))
        return eland_data_mongo_service

    def __delete(self):
        QuerySet(ElandDataDocument,
                 ElandDataDocument().switch_collection("test_aggregate")._get_collection()).delete()

    def __save(self):
        for i in range(2):
            timestamp = int(time.time()) - 2 * 86400
            ElandDataDocument(
                uuid=str(i),
                location=[LocationDocument(region="新加坡", percentage=0)],
                platform=["Mobile"],
                browser=["Line"],
                os=["iOS"],
                gender_tag=Gender.FEMALE,
                geo_tag=Geo.TAIWAN,
                age_tag=Age.TWENTY_FIVE_THIRTY_FOUR,
                income_tag=Income.ONE_HUNDRED,
                create_at=123,
                update_at=100,
                sex=[48.81, 51.19],
                income=[47.77, 23.21, 16.13, 12.89],
                age=[33.0, 22.89, 14.45, 11.53, 18.13],
                habit_weekday=[HabitWeekDayDocument(weekday="Mon", percentage=16.13)],
                habit_hour=[HabitHourDocument(hour=0, percentage=1)],
                month_usage_score=100,
                interest=[InterestDocument(tag="族群:健身族",
                                           score=i + 1)],
                intent=["室內娛樂:DIY手作/手工藝", "軍事:軍事"]
            ).switch_collection("test_aggregate") \
                .save()

    def test_list_collection_names_have_value(self):
        service = self.get_instance()
        self.__save()
        result = service.list_collection_names()

        self.assertEqual(result, ['test_aggregate'])

        self.__delete()

    def test_find_all_by_query_only_empty(self):
        service = self.get_instance()

        result = service.find_all_batch(None, "interest__tag", "族群:健身族", 0, 10000)

        self.assertEqual(len(result), 0)

    def test_find_all_by_query_only(self):
        service = self.get_instance()
        self.__save()

        result = service.find_all_batch("test_aggregate", "interest__tag", "族群:健身族", 0, 10000)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], '0')
        self.assertEqual(result[1][0], '1')
        self.__delete()

