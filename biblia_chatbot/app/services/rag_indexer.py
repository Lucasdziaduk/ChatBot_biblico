import numpy as np
from typing import List, Dict
from app.services.embedding_service import EmbeddingService
from app.services.bible_service import BibleService


class RAGIndexer:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.bible_service = BibleService()
        self.index = []

        self._build_index()

    def _build_index(self):
        print("[RAG] Gerando embeddings da base bíblica...")

        for verse in self.bible_service.data:
            text = verse.get("text", "")
            if not text:
                continue

            embedding = self.embedding_service.get_embedding(text)

            self.index.append({
                "embedding": np.array(embedding),
                "verse": verse
            })

        print(f"[RAG] Index criado com {len(self.index)} versículos")

    def _cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        query_embedding = np.array(
            self.embedding_service.get_embedding(query)
        )

        scored = []

        for item in self.index:
            score = self._cosine_similarity(query_embedding, item["embedding"])
            scored.append((score, item["verse"]))

        scored.sort(reverse=True, key=lambda x: x[0])

        return [v for _, v in scored[:top_k]]