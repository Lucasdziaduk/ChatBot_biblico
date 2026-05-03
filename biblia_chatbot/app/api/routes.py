"""Rotas da API FastAPI."""
from fastapi import APIRouter, Depends, HTTPException

from app.models.schemas import ChatRequest, ChatResponse
from app.services.ai_service import AIService

router = APIRouter()


def get_ai_service() -> AIService:
    from app.main import ai_service
    return ai_service


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest, service: AIService = Depends(get_ai_service)) -> ChatResponse:
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Mensagem vazia.")
    result = service.chat(request.message, request.level, request.history)
    return ChatResponse(**{k: v for k, v in result.items() if k != "error"})


@router.get("/health")
def health() -> dict:
    return {"status": "ok"}
