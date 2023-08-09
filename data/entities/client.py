from peewee import *

from .base import BaseModel

class Client(BaseModel):
    name = CharField(unique=True)
