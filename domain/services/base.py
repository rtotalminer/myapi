from domain.crypto import hash_str

class BasicService():

    def __init__(self, name, entity):
        self.entity = entity
        self.name = name

    def getById(self, id):
        e = self.entity.get(self.entity.id == id)
        return e.__data__