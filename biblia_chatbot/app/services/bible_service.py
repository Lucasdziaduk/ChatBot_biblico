import json
from typing import List, Dict, Any, Optional
from app.core.config import settings


class BibleService:
    def __init__(self):
        self.data_path = settings.bible_data_path
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.data_path, "r", encoding="utf-8-sig") as f:
                raw = json.load(f)

            verses = []

            # 🔥 CASO: lista de livros (SEU CASO)
            if isinstance(raw, list):
                for book_data in raw:
                    if not isinstance(book_data, dict):
                        continue

                    book = book_data.get("abbrev", "unknown").upper()
                    chapters = book_data.get("chapters", [])

                    for c_idx, chapter in enumerate(chapters, start=1):
                        for v_idx, text in enumerate(chapter, start=1):
                            verses.append({
                                "book": book,
                                "chapter": c_idx,
                                "verse": v_idx,
                                "text": text
                            })

            # 🔥 fallback (caso diferente)
            elif isinstance(raw, dict) and "chapters" in raw:
                book = raw.get("abbrev", "unknown").upper()

                for c_idx, chapter in enumerate(raw["chapters"], start=1):
                    for v_idx, text in enumerate(chapter, start=1):
                        verses.append({
                            "book": book,
                            "chapter": c_idx,
                            "verse": v_idx,
                            "text": text
                        })

            print(f"[DEBUG] Versículos carregados: {len(verses)}")
            return verses

        except Exception as e:
            print(f"[ERRO] Falha ao carregar base bíblica: {e}")
            return []
    def search_verses(self, query: str) -> List[Dict[str, Any]]:
        """Busca simples por texto (fallback básico)"""
        results = []
        query = query.lower()

        for verse in self.data:
            if query in verse.get("text", "").lower():
                results.append(verse)

        return results[:5]

    def get_chapter(self, book: str, chapter: int) -> List[Dict[str, Any]]:
        return [
            v for v in self.data
            if v.get("book", "").lower() == book.lower()
            and v.get("chapter") == chapter
        ]

    def find_character(self, name: str) -> Optional[Dict[str, Any]]:
        """Stub inicial — pode evoluir depois"""
        characters = {
            "moisés": "Líder do Êxodo e mediador da Lei.",
            "davi": "Rei de Israel, conhecido por sua fé e arrependimento.",
            "jesus": "Filho de Deus e Salvador da humanidade.",
            "paulo": "Apóstolo dos gentios e autor de várias epístolas."
        }

        desc = characters.get(name.lower())
        if desc:
            return {"name": name, "description": desc}

        return None

    def find_doctrine(self, topic: str) -> Optional[Dict[str, Any]]:
        """Stub inicial — pode evoluir depois"""
        doctrines = {
            "salvação": "A salvação é pela graça mediante a fé (Efésios 2:8).",
            "fé": "A fé é a certeza das coisas que se esperam (Hebreus 11:1).",
            "pecado": "O pecado separa o homem de Deus (Romanos 3:23)."
        }

        desc = doctrines.get(topic.lower())
        if desc:
            return {"topic": topic, "description": desc}

        return None