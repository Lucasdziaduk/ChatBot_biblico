from openai import OpenAI
from app.core.config import settings
from app.services.rag_indexer import RAGIndexer


class AIService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model

        self.rag = RAGIndexer()

        self.system_prompt = """
Você é um especialista em Bíblia.

Use os versículos fornecidos como base principal da resposta.
Explique de forma clara, fiel e prática.

Se houver múltiplos versículos, conecte as ideias.
Evite inventar conteúdo fora da Bíblia.
"""

    def generate_response(self, user_input: str) -> str:
        """
        Fluxo completo com RAG:
        1. Busca semântica
        2. Monta contexto
        3. LLM responde
        """

        try:
            verses = self.rag.search(user_input)

            context = self._format_context(verses)

            prompt = f"""
Pergunta:
{user_input}

Versículos relevantes:
{context}
"""

            response = self.client.responses.create(
                model=self.model,
                input=f"{self.system_prompt}\n\n{prompt}",
            )

            return response.output_text

        except Exception as e:
            print(f"[ERRO RAG/LLM] {e}")
            return self._fallback_response(user_input)

    def _format_context(self, verses):
        lines = []

        for v in verses:
            ref = f"{v.get('book')} {v.get('chapter')}:{v.get('verse')}"
            text = v.get("text")

            lines.append(f"{ref} - {text}")

        return "\n".join(lines)

    def _fallback_response(self, question: str) -> str:
        return (
            "Não consegui gerar uma resposta completa agora. "
            "Tente reformular a pergunta."
        )