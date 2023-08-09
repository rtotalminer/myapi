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

"""
    Handles CRUD methods.
"""

class BasicRouter(BaseRouter):
    def __init__(self, name, model, service):    
        super().__init__(name)
        self.model = model
        self.service = service
        
        # register base routes
        self.router.add_api_route(f"/{self.name}/Get", self.get, methods=["GET"])        
        self.router.add_api_route(f"/{self.name}/Add", self.add, methods=["POST"])
        self.router.add_api_route(f"/{self.name}/Update", self.update, methods=["PUT"])
        self.router.add_api_route(f"/{self.name}/Delete", self.delete, methods=["DELETE"])

    async def get(self, id):
        return self.service.getById(id)

    # TODO: Inherit model and use as a parameter type to avoid constatnly overriding.
    async def add(self, model: object):
        return self.service.add(model)
    
    async def update(self, model: object):
        return self.service.update(model)

    async def delete(self, model: object):
        return self.service.delete(model)
