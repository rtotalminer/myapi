import domain.services.auth as auth
from .base import BaseRouter
from fastapi import HTTPException
from domain.models.register import RegisterModelClient, RegisterModelServer

class AuthRouter(BaseRouter):
    def __init__(self, name):
        super().__init__(name)
        self.router.add_api_route(f"/{self.name}/Login", self.login, methods=["POST"])
        self.router.add_api_route(f"/{self.name}/Register", self.register, methods=["POST"], response_model=RegisterModelServer)

    def login(self):
        pass
    
    
    def register(self, user : RegisterModelClient):
        token = auth.register(user)
        if not (token):
            raise HTTPException(status_code=404, detail="User already exists")
        
        model = RegisterModelServer(username=user.username, jwt_token=token)
        return model
