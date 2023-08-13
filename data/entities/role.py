from peewee import *

from .base import BaseEntity

class Role(BaseEntity):
    name = CharField(unique=True)
    
