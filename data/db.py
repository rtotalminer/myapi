
from peewee import *

import datetime
import sys

from .entities.user import User, UserRole
from .entities.role import Role

sys.path.append("..")
from domain.crypto import hash_pass


db = SqliteDatabase('db.db') 

def db_init():

    db.connect()
    try:
        pass
        db.create_tables([User, Role, UserRole])

        user = User.create(username="superuser", password=hash_pass("password"))
        admin_role = Role.create(name="Admin")
        UserRole.create(user=user, role=admin_role)

    except Exception as e:
        print(e)

