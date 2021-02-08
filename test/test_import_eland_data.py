from mongoengine import connect
import datetime as dt
from document.constant.age import Age
from document.constant.gender import Gender
from document.constant.geo import Geo
from document.constant.income import Income
from document.eland_data_document import ElandDataDocument, LocationDocument, HabitWeekDayDocument, HabitHourDocument, \
    InterestDocument

connect(db="eland_data", host="127.0.0.1", username="admin",
        password="admin",
        authentication_source="admin")

ElandDataDocument(
    uuid="74FAE51867348A0E2AACE2D0CF130C82",
    location=[LocationDocument(region="新加坡", percentage=0)],
    platform=["Mobile"],
    browser=["Line"],
    os=["iOS"],
    gender_tag=Gender.FEMALE,
    geo_tag=Geo.TAIWAN,
    age_tag=Age.TWENTY_FIVE_THIRTY_FOUR,
    income_tag=Income.ONE_HUNDRED,
    create_at=dt.datetime(2021, 1, 1, 0, 0, 0),
    update_at=dt.datetime(2021, 1, 1, 0, 0, 0),
    sex=[48.81, 51.19],
    income=[47.77, 23.21, 16.13, 12.89],
    age=[33.0, 22.89, 14.45, 11.53, 18.13],
    habit_weekday=[HabitWeekDayDocument(weekday="Mon", percentage=16.13)],
    habit_hour=[HabitHourDocument(hour=0, percentage=1)],
    month_usage_score=100,
    interest=[InterestDocument(tag="族群:健身族",
                               score=123)],
    intent=["室內娛樂:DIY手作/手工藝", "軍事:軍事"]
).switch_collection("test_aggregate") \
    .save()
