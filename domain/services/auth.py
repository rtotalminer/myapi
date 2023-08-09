import jwt

from peewee import *

from data.entities.user import User
from domain.models.register import RegisterModelClient

from domain.crypto import hash_str

# TODO: Move to .env
my_secret = 'my_super_secret'


def create_jwt_token(payload_data) -> str:
    token = jwt.encode(
        payload = payload_data,
        key = my_secret
    )
    return token

def register(user : RegisterModelClient):
    # check if user model is valid
    
    # check if user in db  
    is_user = User.select().where(User.username == user.username)  
    if (is_user):
        return False
    
    # create new user
    db = SqliteDatabase('db.db')
    db.connect()
    User.create(username = user.username, password=hash_str(user.password))

    
    # create jwt
    token = create_jwt_token({"username": user.username})
    
    # send back jwt
    return token
    
