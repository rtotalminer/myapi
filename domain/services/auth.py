import jwt

from peewee import *

from data.entities.user import User
from domain.models.user import UserModel

from domain.crypto import hash_pass, check_password
from data.db import db

from fastapi import HTTPException, status


# TODO: Move to .env
my_secret = 'my_super_secret'


def create_jwt_token(payload_data) -> str:
    token = jwt.encode(
        payload = payload_data,
        key = my_secret
    )
    return token

def register(user : UserModel):
    is_user = User.select().where(User.username == user.username)  
    if (is_user):
        return False

    db.connect()
    User.create(username = user.username, password=hash_pass(user.password))

    token = create_jwt_token({"username": user.username})
    return token

def authenticate(user : UserModel):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    user_id = User.select().where(User.username == user.username)

    if not user_id:
        return exception

    _user = User.get(User.id == user_id)

    if not check_password(user.password, _user.password):
        return exception

    return _user.__data__


# def login(user : UserModel) -> Token:
#     user = authenticate_user(**login_data.dict())
#     token_str = create_token(user)
#     token = Token(access_token=token_str, token_type='bearer')
#     return token

    
