from typing import Generic, TypeVar

from domain.models.user import UserModel
import domain.services.user as UserService

from .base import BaseRouter


class UserRouter(BaseRouter):
    def __init__(self, name):
        super().__init__(name)

        self.router.add_api_route(f"/{self.name}/Get", self.get, methods=["GET"])
        self.router.add_api_route(f"/{self.name}/GetAll", self.getAll, methods=["GET"])
    
    def get(self, id):
        res = UserService.get(id)
        return res

    def getAll(self):
        return UserService.getAll()
