from .BaseController import BaseController 

from  fastapi  import UploadFile , status 
from fastapi.responses import JSONResponse

from enums import ResponseSignal 
from .ProjectController import ProjectController
import re
import os 

class DataController(BaseController):
    def __init__(self):
        # Call BaseController
        super().__init__()

    def validate_uploaded_file(self , file : UploadFile ):

        if file.content_type not in self.app_settings.FILE_ALLOWED_EXTENSIONS :
            return False , ResponseSignal.FileTypeNotSupported 
        

        if file.size > self.app_settings.FILE_MAX_SIZE * 1048576 :
            return False , ResponseSignal.FileSizeExceeded 
        
        return True , ResponseSignal.FileUploadedSuccessfully


    def generate_unique_filename(self , filename : str , project_id : str ):
        
        random_filename = self.generate_random_string()
        project_path = ProjectController().get_project_path(str(project_id))
        
        cleaned_file_name = self.get_clean_file_name( filename )
        
        new_file_name =  os.path.join( 
            project_path , 
            random_filename + "_" + cleaned_file_name 
        )
        
        while os.path.exists(new_file_name ):
            random_filename = self.generate_random_string()
            new_file_name =  os.path.join( 
            project_path , 
            random_filename + "_" + cleaned_file_name 
        )
        
        return new_file_name 

            
    
    

    def get_clean_file_name(self, orig_file_name: str):

        # remove any special characters, except underscore and .
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip())

        # replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name
        
        

        
