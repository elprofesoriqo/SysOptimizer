from pydantic import BaseModel

class Process(BaseModel):
    pid: int
    name: str
    memory_usage: float
    cpu_usage: float
