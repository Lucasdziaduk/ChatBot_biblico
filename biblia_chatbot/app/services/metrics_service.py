"""Métricas simples de uso e robustez."""
from __future__ import annotations

from dataclasses import dataclass, field
from statistics import mean
from time import perf_counter


@dataclass
class MetricsService:
    total_messages: int = 0
    errors: int = 0
    ambiguous_questions: int = 0
    correct_references: int = 0
    coherent_answers: int = 0
    response_times: list[float] = field(default_factory=list)
    simulated_satisfaction_scores: list[float] = field(default_factory=list)

    def start_timer(self) -> float:
        return perf_counter()

    def end_timer(self, started_at: float) -> float:
        elapsed = perf_counter() - started_at
        self.response_times.append(elapsed)
        return elapsed

    def record_success(self, has_correct_reference: bool, coherent: bool, satisfaction: float = 0.9) -> None:
        self.total_messages += 1
        if has_correct_reference:
            self.correct_references += 1
        if coherent:
            self.coherent_answers += 1
        self.simulated_satisfaction_scores.append(max(0.0, min(1.0, satisfaction)))

    def record_error(self) -> None:
        self.total_messages += 1
        self.errors += 1

    def record_ambiguity(self) -> None:
        self.ambiguous_questions += 1

    def get_metrics(self) -> dict:
        total = max(1, self.total_messages)
        avg_time = mean(self.response_times) if self.response_times else 0.0
        avg_satisfaction = mean(self.simulated_satisfaction_scores) if self.simulated_satisfaction_scores else 0.0
        return {
            "precision": {
                "taxa_referencia_correta": round(self.correct_references / total, 3),
                "taxa_respostas_coerentes": round(self.coherent_answers / total, 3),
            },
            "ux": {
                "tempo_medio_resposta": round(avg_time, 4),
                "satisfacao_simulada": round(avg_satisfaction, 3),
                "quantidade_mensagens": self.total_messages,
            },
            "robustez": {
                "taxa_erro": round(self.errors / total, 3),
                "taxa_ambiguidade": round(self.ambiguous_questions / total, 3),
            },
        }
