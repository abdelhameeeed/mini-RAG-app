from pydantic import BaseModel
from typing import Optional 

# Make Sure parameters pass to the API is indeed with this datatypes 
class ProcessRequest(BaseModel):
    file_id : str 
    chunck_size : Optional[int] = 5 
    overalp_size : Optional[int] = 1
    do_reset: Optional[int] = 0 
    
