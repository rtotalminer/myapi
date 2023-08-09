
from peewee import *
import datetime
import sys
from .entities.user import User

sys.path.append("..")
from domain.crypto import hash_str


def db_init():
    
    db = SqliteDatabase('db.db')

    db.connect()
    try:
        db.create_tables([User])
        User.create(username="admin", password=hash_str("password"))
    except Exception as e:
        print(e)
