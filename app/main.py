from fastapi import FastAPI
from app.routes import monitor, optimize, clean, summary

app = FastAPI()

# Rejestracja endpointów
app.include_router(monitor.router, prefix="/monitor", tags=["Monitor"])
app.include_router(optimize.router, prefix="/optimize", tags=["Optimize"])
app.include_router(clean.router, prefix="/clean", tags=["Clean"])
app.include_router(summary.router, prefix="/summary", tags=["Summary"])
