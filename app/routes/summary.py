from fastapi import APIRouter
from app.services.summary_service import generate_summary

router = APIRouter()

@router.get("/")
async def summary():
    """
    Generuje podsumowanie działań i stanu systemu.
    """
    summary_data = generate_summary()
    return {"summary": summary_data}
