from .BaseController import BaseController 
from  fastapi  import UploadFile , status 
from fastapi.responses import JSONResponse
import os 
from enums import ResponseSignal 

class ProjectController(BaseController):
    def __init__(self):
        # Call BaseController
        super().__init__()

    def get_project_path(self , project_id):

        project_path = os.path.join( 
            self.assests_files_path  , 
            str(project_id)
        )
        if not os.path.exists(project_path):
            os.makedirs(project_path)
        
        return project_path