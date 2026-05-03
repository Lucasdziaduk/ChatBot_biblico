# Bíblia Chatbot Adventista

Projeto acadêmico em Python para um chatbot bíblico com foco na perspectiva da Igreja Adventista do Sétimo Dia.

## Funcionalidades
- Perguntas sobre versículos, personagens, doutrinas, profecias e contexto histórico
- Respostas em três níveis: simples, completa e profunda
- Classificação automática da intenção
- Base bíblica local em JSON
- API com FastAPI
- Interface em Gradio
- Métricas e testes com pytest

## Estrutura
```text
biblia_chatbot/
├── app/
├── ui/
├── tests/
├── requirements.txt
└── README.md
```

## Instalação
```bash
pip install -r requirements.txt
```

## Execução da API
```bash
uvicorn app.main:app --reload
```

## Execução da interface
Em outro terminal:
```bash
python ui/gradio_app.py
```

## Exemplo de requisição
```json
{
  "message": "O que significa João 3:16?",
  "level": "completa"
}
```

## Exemplo de resposta
```json
{
  "response": "1. Resposta direta: ...",
  "references": ["João 3:16"],
  "question_type": "versiculo"
}
```

## Testes
```bash
pytest
```

## Melhorias futuras
- Integração com LLM real
- Busca semântica sobre uma base bíblica ampliada
- Memória de conversa persistente
- Suporte a múltiplas traduções bíblicas
- Painel analítico de métricas
