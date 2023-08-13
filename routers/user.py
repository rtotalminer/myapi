from typing import Generic, TypeVar

from domain.models.user import UserModel
from .base import BaseRouter


class UserRouter(BaseRouter):
    def __init__(self, name):
        super().__init__(name)

        self.router.add_api_route(f"/{self.name}/GetAll", self.getAll, methods=["GET"])
        self.router.add_api_route(f"/{self.name}/Add", self.add, methods=["POST"])
    
    def add(self):
        e = self.service.add()
        return e

    def getAll(self):
        return self.service.getAll()
