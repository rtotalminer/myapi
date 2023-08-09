from .base import BasicRouter

class ClientRouter(BasicRouter):
    def __init__(self, name, service):
        super().__init__(name, service)
    
