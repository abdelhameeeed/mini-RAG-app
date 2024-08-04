from enum import Enum 

class ResponseSignal(Enum):
    
    FileTypeNotSupported = "File Type Not Supported"
    
    FileSizeExceeded = "File Size Exceeded"
    
    FileUploadedSuccessfully = "File Uploaded Successfully"
    
    FileUploadFailed = "File Uploaded Failed"
    
    FileProcessingFailed = "File Processing Failed"

    FileProcessingSucess = "File Processing Sucess"
    
    