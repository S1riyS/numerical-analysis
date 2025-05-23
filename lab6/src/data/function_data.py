from math import cos, exp, sin

from models.function_data import FunctionData

data = [
    FunctionData(
        str_expr="sin(x) - y",
        func=lambda x, y: sin(x) - y,
        exact_solution=lambda x, x0, y0: (2 * exp(x0) * y0 - exp(x0) * sin(x0) + exp(x0) * cos(x0))
        / (2 * exp(x))
        + (sin(x)) / 2
        - (cos(x)) / 2,
    ),
    FunctionData(
        str_expr="e^x",
        func=lambda x, y: exp(x),
        exact_solution=lambda x, x0, y0: y0 - exp(x0) + exp(x),
    ),
    FunctionData(
        str_expr="x + y",
        func=lambda x, y: x + y,
        exact_solution=lambda x, x0, y0: exp(x - x0) * (y0 + x0 + 1) - x - 1,
    ),
    FunctionData(
        str_expr="y + (1 + x) * y^2",
        func=lambda x, y: y + (1 + x) * y**2,
        exact_solution=lambda x, x0, y0: -exp(x)
        / (x * exp(x) - (x0 * exp(x0) * y0 + exp(x0)) / y0),
    ),
]
