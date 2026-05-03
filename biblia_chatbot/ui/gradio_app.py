
"""Interface Gradio consumindo a API FastAPI."""
from __future__ import annotations

import os
from typing import List, Tuple

import gradio as gr
import requests

API_URL = os.getenv("BIBLIA_CHATBOT_API_URL", "http://127.0.0.1:8000")


def send_message(message: str, history: List[Tuple[str, str]], level: str):
    """Envia a pergunta para a API e retorna o histórico atualizado."""
    history = history or []
    if not message.strip():
        return history, history, ""

    payload = {"message": message, "level": level, "history": []}
    try:
        response = requests.post(f"{API_URL}/chat", json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        answer = data["response"]
    except Exception as exc:
        answer = f"Erro ao conectar à API: {exc}"

    history = history + [(message, answer)]
    return history, history, ""


def clear_chat():
    return [], [], ""


with gr.Blocks(title="Chat Bíblico Adventista") as demo:
    gr.Markdown("# Chat Bíblico Adventista")
    gr.Markdown("Assistente bíblico com foco adventista, histórico, referências e respostas em três níveis.")
    chatbot = gr.Chatbot(height=520)
    state = gr.State([])

    with gr.Row():
        msg = gr.Textbox(label="Pergunta", placeholder="Ex.: O que significa João 3:16?")
    with gr.Row():
        level = gr.Radio(choices=["simples", "completa", "profunda"], value="completa", label="Nível da resposta")
    with gr.Row():
        send_btn = gr.Button("Enviar")
        clear_btn = gr.Button("Limpar histórico")

    send_btn.click(send_message, inputs=[msg, state, level], outputs=[chatbot, state, msg])
    msg.submit(send_message, inputs=[msg, state, level], outputs=[chatbot, state, msg])
    clear_btn.click(clear_chat, outputs=[chatbot, state, msg])

if __name__ == "__main__":
    demo.launch()
