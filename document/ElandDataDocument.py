from mongoengine import DynamicEmbeddedDocument, StringField, FloatField, IntField, DynamicDocument, ListField, \
    EmbeddedDocumentField


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
    meta = {
        "collection": "20210201"
    }
    uuid = StringField()
    location = ListField(EmbeddedDocumentField(LocationDocument))
    platform = ListField()
    browser = ListField()
    os = ListField()
    sex = ListField()
    income = ListField()
    age = ListField()
    habit_weekday = ListField(EmbeddedDocumentField(HabitWeekDayDocument))
    habit_hour = ListField(EmbeddedDocumentField(HabitHourDocument))
    month_usage_score = FloatField()
    interest = ListField(EmbeddedDocumentField(InterestDocument))
    intent = ListField()