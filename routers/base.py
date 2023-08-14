from typing import Generic, TypeVar
from fastapi import APIRouter, Request, Depends

from domain.models.user import UserModel

from fastapi_utils.cbv import cbv

"""
    Base Router is very basic and just create a name and router.
"""
class BaseRouter():
    def __init__(self, name):
        self.name = name
        self.router = APIRouter(tags=[self.name])
