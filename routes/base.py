from fastapi import FastAPI , APIRouter
import os 

base_router = APIRouter(
    prefix = '/api/v1' ,
    tags = ['api_v1']
)

@base_router.get("/")
async def homepage():
    return { os.getenv('APP_NAME') : os.getenv('APP_VERSION') } 

