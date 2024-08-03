from helpers.config import  get_settings , Settings 

import os 
import random
import string


class BaseController :
    def __init__(self):
        self.app_settings = get_settings()
        self.parent_path = os.path.dirname( os.path.dirname(__file__))
        self.assests_files_path = os.path.join( self.parent_path  ,  'assests/files' ) 

    def generate_random_string(self, length: int=12):
            return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))