import psutil

from app.config import db
from datetime import datetime

def generate_summary():
    """
    Generuje podsumowanie na podstawie logów i bieżącego stanu systemu.
    """
    logs = list(db.logs.find().sort("timestamp", -1).limit(10))  # Pobierz 10 ostatnich logów
    total_memory = psutil.virtual_memory().total / (1024 * 1024 * 1024)  # GB
    available_memory = psutil.virtual_memory().available / (1024 * 1024 * 1024)  # GB
    cpu_usage = psutil.cpu_percent(interval=1)

    summary = {
        "recent_logs": logs,
        "memory": {
            "total": total_memory,
            "available": available_memory
        },
        "cpu_usage": cpu_usage,
        "timestamp": datetime.now().isoformat()
    }
    return summary
