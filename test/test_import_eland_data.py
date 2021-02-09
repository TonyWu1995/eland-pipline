import time

from mongoengine import connect

from constant.age import Age
from constant.gender import Gender
from constant.geo import Geo
from constant.income import Income
from document.eland_data_document import ElandDataDocument, LocationDocument, HabitWeekDayDocument, HabitHourDocument, \
    InterestDocument

# https://stackoverflow.com/questions/58231798/bulk-write-in-mongoengine
connect(db="eland_data", host="192.168.101.41", username="admin",
        password="admin",
        authentication_source="admin")

for i in range(1, 101):
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
        update_at=timestamp,
        sex=[48.81, 51.19],
        income=[47.77, 23.21, 16.13, 12.89],
        age=[33.0, 22.89, 14.45, 11.53, 18.13],
        habit_weekday=[HabitWeekDayDocument(weekday="Mon", percentage=16.13)],
        habit_hour=[HabitHourDocument(hour=0, percentage=1)],
        month_usage_score=100,
        interest=[InterestDocument(tag="族群:健身族",
                                   score=i)],
        intent=["室內娛樂:DIY手作/手工藝", "軍事:軍事"]
    ).switch_collection("test_aggregate") \
        .save()
