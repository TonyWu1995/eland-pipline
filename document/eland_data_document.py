from mongoengine import DynamicEmbeddedDocument, StringField, FloatField, IntField, DynamicDocument, ListField, \
    EmbeddedDocumentField, DateTimeField, EnumField

from document.constant.age import Age
from document.constant.gender import Gender
from document.constant.geo import Geo
from document.constant.income import Income


class InterestDocument(DynamicEmbeddedDocument):
    tag = StringField()
    score = FloatField()


class LocationDocument(DynamicEmbeddedDocument):
    region = StringField()
    percentage = FloatField()


class HabitWeekDayDocument(DynamicEmbeddedDocument):
    weekday = StringField()
    percentage = FloatField()


class HabitHourDocument(DynamicEmbeddedDocument):
    hour = IntField()
    percentage = FloatField()



class ElandDataDocument(DynamicDocument):
    uuid = StringField()
    location = ListField(EmbeddedDocumentField(LocationDocument))
    platform = ListField()
    browser = ListField()
    os = ListField()
    gender_tag = EnumField(Gender)
    income_tag = EnumField(Income)
    age_tag = EnumField(Age)
    create_at = DateTimeField()
    update_at = DateTimeField()
    geo_tag = EnumField(Geo)
    sex = ListField()
    income = ListField()
    age = ListField()
    habit_weekday = ListField(EmbeddedDocumentField(HabitWeekDayDocument))
    habit_hour = ListField(EmbeddedDocumentField(HabitHourDocument))
    month_usage_score = FloatField()
    interest = ListField(EmbeddedDocumentField(InterestDocument))
    intent = ListField()
