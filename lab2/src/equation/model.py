import matplotlib.pyplot as plt
import numpy as np

from types_ import Math1DFunction  # type: ignore


class Equation:
    def __init__(self, function: Math1DFunction, text: str):
        self.text = text
        self.function = np.vectorize(function)

    def root_exists(self, left: float, right: float):
        return self.function(left) * self.function(right) < 0

    def __repr__(self) -> str:
        return self.text
