import math
from typing import Callable, List


def compute_mean_squared_error(xs: List[float], ys: List[float], fi: Callable[[float], float]) -> float:
    n = len(xs)
    return math.sqrt(sum(((fi(xi) - yi) ** 2 for xi, yi in zip(xs, ys))) / n)


def compute_measure_of_deviation(xs: List[float], ys: List[float], fi: Callable[[float], float]) -> float:
    epsilons = [fi(xi) - yi for xi, yi in zip(xs, ys)]
    return sum((eps**2 for eps in epsilons))


def compute_coefficient_of_determination(xs: List[float], ys: List[float], fi: Callable[[float], float]) -> float:
    n = len(xs)
    avg_fi = sum(fi(x) for x in xs) / n

    numerator = sum((y - avg_fi) ** 2 for y in ys)
    denominator = sum((y - fi(x)) ** 2 for x, y in zip(xs, ys))

    # If fi is equivalent to actual function: R^2 = 1
    if denominator == 0:
        return 1
    return 1 - numerator / denominator


def compute_pearson_correlation(xs: List[float], ys: List[float]) -> float:
    n = len(xs)
    avg_x = sum(xs) / n
    avg_y = sum(ys) / n

    numerator = sum((x - avg_x) * (y - avg_y) for x, y in zip(xs, ys))
    denominator = math.sqrt(sum((x - avg_x) ** 2 for x in xs) * sum((y - avg_y) ** 2 for y in ys))
    return numerator / denominator
