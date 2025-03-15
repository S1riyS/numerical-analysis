import numpy as np

from types_ import Math2DFunction  # type: ignore


class System:
    def __init__(self, f1: Math2DFunction, f2: Math2DFunction, text: str):
        self.f1 = np.vectorize(f1)
        self.f2 = np.vectorize(f2)
        self.text = text

    def __repr__(self) -> str:
        return self.text
