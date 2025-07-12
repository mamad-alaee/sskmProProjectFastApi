from mongoengine import Document,StringField


class User(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True) 