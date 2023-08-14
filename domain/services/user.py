
from data.entities.user import User

def get(_id):
    e = User.get(User.id == _id)
    return e.__data__