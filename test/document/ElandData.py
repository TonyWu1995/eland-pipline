from mongoengine import DynamicEmbeddedDocument, StringField, FloatField, IntField, DynamicDocument, ListField, \
    EmbeddedDocumentField


class Interest(DynamicEmbeddedDocument):
    tag = StringField()
    score = FloatField()


class Location(DynamicEmbeddedDocument):
    region = StringField()
    percentage = FloatField()


class HabitWeekDay(DynamicEmbeddedDocument):
    weekday = StringField()
    percentage = FloatField()


class HabitHour(DynamicEmbeddedDocument):
    hour = IntField()
    percentage = FloatField()


class ElandData(DynamicDocument):
    meta = {
        "collection": "20210201"
    }
    uuid = StringField()
    location = ListField(EmbeddedDocumentField(Location))
    platform = ListField()
    browser = ListField()
    os = ListField()
    sex = ListField()
    income = ListField()
    age = ListField()
    habit_weekday = ListField(EmbeddedDocumentField(HabitWeekDay))
    habit_hour = ListField(EmbeddedDocumentField(HabitHour))
    month_usage_score = FloatField()
    interest = ListField(EmbeddedDocumentField(Interest))
    intent = ListField()
