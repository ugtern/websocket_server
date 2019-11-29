from datetime import datetime
from pymongo import MongoClient
from umongo import Instance, Document, fields, validate

db = MongoClient('mongodb://websocket_server_db:27017').test
instance = Instance(db)


@instance.register
class User(Document):

    login = fields.StrField(required=True, unique=True)
    password = fields.StrField()

    class Meta:
        collection = db.user
