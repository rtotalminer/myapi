from pydantic import BaseModel

class RegisterModelClient(BaseModel):
    username : str
    password: str
    
class RegisterModelServer(BaseModel):
    username: str
    jwt_token: str