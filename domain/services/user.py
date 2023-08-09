
from data.entities.user import User
from domain.services.base import BasicService


class UserService(BasicService):
    def __init__(self, name, entity):
        super().__init__(name, entity)