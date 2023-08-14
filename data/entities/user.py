from peewee import *

from .base import BaseEntity
from .role import Role

class User(BaseEntity):
    username = CharField(unique=True)
    password = CharField(unique=False)
    
class UserRole(BaseEntity):
    user = ForeignKeyField(User)
    role = ForeignKeyField(Role)