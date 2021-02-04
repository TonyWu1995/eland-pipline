from mongoengine import connect, StringField, DynamicDocument, ListField
from mongoengine.queryset import QuerySet

c = connect(db='eland_test', host='192.168.101.41', port=27017, username="admin", password="admin",
            authentication_source="admin")


# c.list_collections()


class ElandData(DynamicDocument):
    meta = {
        "collection": "eland_20210203"
    }
    uuid = StringField()
    location = ListField()


old_objects = QuerySet(ElandData, ElandData._get_collection())
for row in old_objects.all():
    print('old', row.uuid, row.location)
# print(ElandData.objects.count())
# print(ElandData().switch_collection("test"))

# print(d.objects.__dict__)


new_objects = QuerySet(ElandData, ElandData().switch_collection("test")._get_collection())

print(new_objects.all())
print('a', new_objects.get(uuid="11").uuid)
for elandData in new_objects.filter(uuid="112").all():
    print(elandData.uuid)

new_objects = QuerySet(ElandData, ElandData().switch_collection("eland_20210201")._get_collection())

for elandData in new_objects:
    print(elandData.uuid)
