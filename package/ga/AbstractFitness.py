from typing import List
from abc import ABC, abstractmethod


class AbstractFitness(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self, individual: List[any], iterations: int = 1000, display_logging: bool = False) -> float:
        pass
