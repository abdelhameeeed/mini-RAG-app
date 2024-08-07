from fastapi import FastAPI , APIRouter , Depends , UploadFile , status
from helpers.config import  get_settings , Settings 
import os 
from controllers import DataController , ProjectController , ProcessController 
from enums import ResponseSignal 

from fastapi.responses import JSONResponse
import os 
import aiofiles
import logging

from schemas.data import ProcessRequest 


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
    
    file_path , file_id = DataController().generate_unique_filename(file.filename , str(project_id))
    
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
                'Signal' : signal.value , 
                'file_id' : file_id 
            }
        )



@data_router.post('/process/{project_id}')
async def process_file(project_id: str , process_request : ProcessRequest ):
     file_id =  process_request.file_id 
     chunck_size = process_request.chunck_size 
     overlap_size = process_request.overalp_size


     try:
          
        process_controller = ProcessController(project_id= project_id)
        file_content = process_controller.get_file_content(file_id=file_id)


        chunks = process_controller.process_file_content(file_content 
                                                        , file_id=file_id  
                                                        ,chunk_size=chunck_size
                                                        ,overlap_size=overlap_size)
     
        if len(chunks) == 0 or chunks == None :
                
                return JSONResponse( 
                
                status_code = status.HTTP_400_BAD_REQUEST,
                content = {
                    'Signal' : ResponseSignal.FileProcessingFailed.value  
                }
            )
        
        return chunks
     
     except:
             return JSONResponse( 
                
                status_code = status.HTTP_400_BAD_REQUEST,
                content = {
                    'Signal' : ResponseSignal.FileProcessingFailed.value  
                }
            )
          

