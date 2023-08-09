from peewee import *

from .base import BaseModel

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField(unique=False)
    salt = CharField(unique=False)
