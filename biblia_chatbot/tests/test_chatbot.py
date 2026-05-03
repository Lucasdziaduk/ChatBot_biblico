
"""Testes do chatbot."""
from pathlib import Path
import sys

from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.main import app  # noqa: E402

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat_verse():
    payload = {"message": "O que significa João 3:16?", "level": "completa"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "João 3:16" in data["references"]
    assert "Resposta direta" in data["response"]


def test_chat_character():
    payload = {"message": "Quem foi Moisés?", "level": "simples"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "Moisés" in data["response"]


def test_invalid_message():
    payload = {"message": "", "level": "completa"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 422 or response.status_code == 400


def test_ambiguous_question():
    payload = {"message": "Explique isso", "level": "completa"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["needs_clarification"] is True
