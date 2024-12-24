from fastapi import APIRouter
from app.services.optimize_service import optimize_memory, optimize_cpu

router = APIRouter()

@router.post("/memory")
async def optimize_memory_route():
    """
    Optymalizuje użycie pamięci RAM.
    """
    result = optimize_memory()
    return {"status": "success", "details": result}

@router.post("/cpu")
async def optimize_cpu_route():
    """
    Optymalizuje wykorzystanie CPU.
    """
    result = optimize_cpu()
    return {"status": "success", "details": result}
