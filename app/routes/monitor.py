from fastapi import APIRouter
from app.services.monitor_service import get_processes

router = APIRouter()

@router.get("/processes")
async def monitor_processes():
    """
    Endpoint zwracający listę procesów działających w systemie.
    """
    processes = get_processes()
    return {"processes": processes}
