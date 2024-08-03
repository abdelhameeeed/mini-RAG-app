from fastapi import FastAPI , APIRouter , Depends
from helpers.config import  get_settings , Settings 
import os 


base_router = APIRouter(
    prefix = '/api/v1' ,
    tags = ['api_v1']
)


@base_router.get("/")
async def homepage(app_settings:Settings = Depends(get_settings)):
    return { 
        'App_name' : app_settings.APP_NAME , 
        'App_version' : app_settings.APP_VERSION 
        
     } 

