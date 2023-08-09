
class BasicService():

    def __init__(self, name, entity):
        self.entity = entity
        self.name = name

    def getById(self, id):
        e = self.entity.get(self.entity.id == id)
        return e.__data__
        
    def add(self):
        pass

    def bulkAdd(self):
        pass

    def update(self):
        pass
    
    def delete(self):
        pass

    def bulkDelete(self):
        pass

    def count(self):
        pass
