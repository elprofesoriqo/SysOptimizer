from fastapi import APIRouter
from app.services.clean_service import analyze_files, clean_files

router = APIRouter()

@router.post("/analyze")
async def analyze_cleanup():
    """
    Analizuje pliki do usunięcia.
    """
    files = analyze_files()
    return {"files": files}

@router.post("/execute")
async def execute_cleanup():
    """
    Usuwa pliki wskazane przez użytkownika.
    """
    result = clean_files()
    return {"status": result}
