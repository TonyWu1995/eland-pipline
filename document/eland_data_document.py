from mongoengine import DynamicEmbeddedDocument, StringField, FloatField, IntField, DynamicDocument, ListField, \
    EmbeddedDocumentField, EnumField

from constant.age import Age
from constant.gender import Gender
from constant.geo import Geo
from constant.income import Income


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
    geo_tag = EnumField(Geo)
    create_at = IntField()
    update_at = IntField()
    sex = ListField()
    income = ListField()
    age = ListField()
    habit_weekday = ListField(EmbeddedDocumentField(HabitWeekDayDocument))
    habit_hour = ListField(EmbeddedDocumentField(HabitHourDocument))
    month_usage_score = FloatField()
    interest = ListField(EmbeddedDocumentField(InterestDocument))
    intent = ListField()
