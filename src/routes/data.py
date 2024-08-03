from fastapi import FastAPI , APIRouter , Depends , UploadFile
from helpers.config import  get_settings , Settings 
import os 
from controllers import DataController 


data_router = APIRouter(
    prefix = '/api/v1/data' ,
    tags = ['api_v1' , 'data']
)

@data_router.post('/upload/{project_id}')
async def upload_data(project_id : int 
                      , file : UploadFile 
                      , app_settings : Settings = Depends( get_settings) ):
    
    
    
    
    #Validate file properties
    is_valid , signal = DataController().validate_uploaded_file(file)
    return is_valid  , signal , file 


