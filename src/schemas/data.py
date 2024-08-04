from pydantic import BaseModel
from typing import Optional 

# Make Sure parameters pass to the API is indeed with this datatypes 
class ProcessRequest(BaseModel):
    file_id : str 
    chunck_size : Optional[int] = 100 
    overalp : Optional[int] = 20
    do_reset: Optional[int] = 0 
    
