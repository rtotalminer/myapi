from typing import Generic, TypeVar

from domain.models.user import UserModel
from .base import BasicRouter


class UserRouter(BasicRouter):
    def __init__(self, name, model, service):
        super().__init__(name, model, service)
    
    def add(self, model: UserModel):
        return model
