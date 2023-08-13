from fastapi import APIRouter



from . import auth, user

from data.entities.user import User
from domain.models.user import UserModel
from domain.services.user import UserService



router = APIRouter()

def include_api_routes():

    auth_router = auth.AuthRouter("Auth")
    user_router = user.UserRouter("User")

    #client_router = client.ClientRouter("Client", ClientService("Client", Client, ClientModel))
    
    router.include_router(auth_router.router)
    router.include_router(user_router.router)
    #router.include_router(client_router.router)

include_api_routes()