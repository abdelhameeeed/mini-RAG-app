from .BaseController import BaseController 

from  fastapi  import UploadFile

class DataController(BaseController):
    def __init__(self):
        # Call BaseController
        super().__init__()

    def validate_uploaded_file(self , file : UploadFile ):

        if file.content_type not in self.app_settings.FILE_ALLOWED_EXTENSIONS :
            return False , "File Type Not Supported"
        

        if file.size > self.app_settings.FILE_MAX_SIZE * 1048576 :
            return False , 'File Size Exceeded'
        
        return True , 'Sucess'

        
