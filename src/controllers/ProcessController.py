from .BaseController import BaseController 
from .ProjectController import ProjectController 
import os

from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from enums import ExtensionsEnums 


class ProcessController(BaseController):
    def __init__(self , project_id):
        # Call BaseController
        super().__init__()

        self.project_id =  project_id
        self.project_path = ProjectController().get_project_path(self.project_path)

    def get_file_extension(self , file_id : str ):
        return os.path.splitext( file_id )[-1]
    
    def get_file_loader(self , file_id : str  ):

        file_path = os.path.join(

            self.project_path , file_id 
        )

        file_Extension  = self.get_file_extension( file_id= file_id )

        if file_Extension == ExtensionsEnums.EXTENSTION_TXT.value :
            TextLoader(file_path , encoding = 'utf-8')
        
        if file_Extension == ExtensionsEnums.EXTENSTION_PDF.value :
            return PyMuPDFLoader(file_path)
        
        return None 
    
    def get_file_content(self , file_id ):
        loader  = self.get_file_loader( file_id=file_id)

        

