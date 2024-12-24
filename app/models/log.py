from pydantic import BaseModel
from datetime import datetime

class Log(BaseModel):
    timestamp: datetime
    action: str
    status: str
    details: dict
