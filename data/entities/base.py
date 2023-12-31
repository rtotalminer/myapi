from peewee import *

import datetime

db = SqliteDatabase('db.db')

class BaseEntity(Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

