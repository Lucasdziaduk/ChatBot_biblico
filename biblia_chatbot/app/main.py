"""Aplicação principal FastAPI."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.services.ai_service import AIService
from app.services.bible_service import BibleService
from app.services.metrics_service import MetricsService

app = FastAPI(title="Biblia Chatbot API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bible_service = BibleService()
metrics_service = MetricsService()
ai_service = AIService()

app.include_router(router)


@app.get("/")
def root() -> dict:
    return {
        "message": "Biblia Chatbot API em execução",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/metrics")
def metrics() -> dict:
    return metrics_service.get_metrics()
