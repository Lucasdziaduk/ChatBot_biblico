"""Schemas Pydantic da API."""
from enum import Enum
from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class ResponseLevel(str, Enum):
    simples = "simples"
    completa = "completa"
    profunda = "profunda"


class QuestionType(str, Enum):
    versiculo = "versiculo"
    personagem = "personagem"
    doutrina = "doutrina"
    profecia = "profecia"
    contexto_historico = "contexto_historico"
    aplicacao_pratica = "aplicacao_pratica"
    ambigua = "ambigua"


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)
    level: ResponseLevel = ResponseLevel.completa
    history: List[ChatMessage] = Field(default_factory=list)


class ChatResponse(BaseModel):
    response: str
    references: List[str] = Field(default_factory=list)
    question_type: QuestionType
    answer_level: ResponseLevel
    confidence: float
    needs_clarification: bool = False
    metrics: dict = Field(default_factory=dict)
