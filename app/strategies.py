from abc import ABC, abstractmethod
from app.config import WEIGHTS

class BaseGradingStrategy(ABC):
    @abstractmethod
    def compute_initial_grade(self, ww_score: float, pt_score: float, qa_score: float) -> float:
        pass

class StandardDepEdStrategy(BaseGradingStrategy):
    def __init__(self, category: str):
        if category not in WEIGHTS:
            raise ValueError(f"Invalid category '{category}'. Available: {list(WEIGHTS.keys())}")
        self.weights = WEIGHTS[category]

    def compute_initial_grade(self, ww_score: float, pt_score: float, qa_score: float) -> float:
        ww_weighted = ww_score * self.weights["WW"]
        pt_weighted = pt_score * self.weights["PT"]
        qa_weighted = qa_score * self.weights["QA"]
        return round(ww_weighted + pt_weighted + qa_weighted, 2)
