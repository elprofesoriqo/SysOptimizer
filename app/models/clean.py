from pydantic import BaseModel

class CleanFile(BaseModel):
    path: str
    size: float
    file_type: str
    last_accessed: str
