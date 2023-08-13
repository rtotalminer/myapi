from fastapi import APIRouter



from . import auth, user

from data.entities.user import User
from domain.models.user import UserModel



router = APIRouter()

def include_api_routes():
    auth_router = auth.AuthRouter("Auth")
    user_router = user.UserRouter("User")

    router.include_router(auth_router.router)
    router.include_router(user_router.router)

include_api_routes()