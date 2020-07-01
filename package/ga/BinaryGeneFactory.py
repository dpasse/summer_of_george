import numpy as np
from typing import List
from ..transformers.IntegerToBinaryString import IntegerToBinaryString


class BinaryGeneFactory(object):

    def __init__(self, binary_start: int, binary_end: int, max_binary_length: int):
        self.binary_start = binary_start
        self.binary_end = binary_end
        self.transformer = IntegerToBinaryString(max_binary_length)

    def create(self) -> str:
        random_integer = np.random.randint(self.binary_start, self.binary_end)
        return self.transformer.transform(random_integer)

    def create_many(self, total: int) -> List[str]:
        return [ self.create() for _ in range(total) ]
