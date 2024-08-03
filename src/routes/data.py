from fastapi import FastAPI , APIRouter , Depends , UploadFile , status
from helpers.config import  get_settings , Settings 
import os 
from controllers import DataController 
from controllers import ProjectController 
from enums import ResponseSignal 

from fastapi.responses import JSONResponse
import os 
import aiofiles
import logging

logger = logging.getLogger('uvicorn.error')



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
    
    if not is_valid :    
        return JSONResponse( 
            
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {
                'Signal' : signal.value 
            }
        )
    

    # project_dir_path = ProjectController().get_project_path(project_id)
    
    file_path = DataController().generate_unique_filename(file.filename , str(project_id))
    
    try:       
        async with aiofiles.open( file_path , mode='wb') as f:
            while chunk:= await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE ):
                await f.write(chunk)
            
    except Exception as e :
            
            logger.error( f"error while uploading file {e}")
            
            return JSONResponse( 
            
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {
                'Signal' : ResponseSignal.FileUploadFailed.value  
            }
        )
    
        
    return JSONResponse (
        content = {
                'Signal' : signal.value
            }
        
    )

