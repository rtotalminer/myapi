from fastapi import FastAPI

from routers.api import router as router_api

from typing import List

from starlette.config import Config

from starlette.datastructures import CommaSeparatedStrings, Secret

from fastapi.security import OAuth2PasswordBearer

from data import db



###
# Properties configurations
###

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Authorization"

config = Config(".env")

ROUTE_PREFIX_V1 = "/v1"

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast = CommaSeparatedStrings,
    default = "",
)

def run_tests():
    pass

# Configure, start and returns the application
def startup() -> FastAPI:
    
    # Start The FastAPI App
    app = FastAPI()

    # Initialise our database
    db.db_init()

    # Middleware
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    # Mapping all API routes
    app.include_router(router_api, prefix=API_PREFIX)

    return app

app = startup()

