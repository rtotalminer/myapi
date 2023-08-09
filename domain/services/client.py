
from domain.services.base import BasicService


class ClientService(BasicService):
    def __init__(self, name, entity):
        super().__init__(name, entity)