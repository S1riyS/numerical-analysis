from typing import Tuple

import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy.typing import NDArray
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from libs.ode.types import Function1D
from schemas.ode import ODEResponseSchema


def smart_ylim(y: NDArray[np.float64], margin: float = 0.1) -> Tuple[float, float]:
    """Автоматически определяет границы, исключая выбросы"""
    y_finite = y[np.isfinite(y)]  # Игнорируем nan/inf
    if len(y_finite) == 0:
        return (-1, 1)

    q_low, q_high = np.quantile(y_finite, [0.01, 0.99])  # 5% и 95% квантили
    span = q_high - q_low
    return (q_low - margin * span, q_high + margin * span)


class PlotWidget(QWidget):
    EXACT_SOLUTION_N = 5000

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def _should_show_axis(self, values: NDArray[np.float64], threshold_ratio: float = 0.1) -> bool:
        """Determine if axis should be shown based on proximity to zero"""
        if len(values) == 0:
            return False

        finite_values = values[np.isfinite(values)]
        if len(finite_values) == 0:
            return False

        value_range = np.max(finite_values) - np.min(finite_values)
        threshold = threshold_ratio * value_range

        return (np.min(finite_values) <= threshold) and (np.max(finite_values) >= -threshold)  # type: ignore

    def plot_solution(
        self,
        response: ODEResponseSchema,
        exact_solution: Function1D | None = None,
    ) -> None:
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Plot numerical solution
        ax.plot(response.xs, response.ys, "b-", label="Численное решение")

        # Get all y values that might be plotted
        all_ys = response.ys.copy()
        all_xs = response.xs.copy()

        # Plot exact solution if provided
        if exact_solution is not None:
            exact_xs = np.linspace(
                response.xs[0],
                response.xs[-1],
                self.EXACT_SOLUTION_N,
            )
            exact_ys = np.vectorize(exact_solution)(exact_xs)
            ax.plot(exact_xs, exact_ys, "r--", label="Точное решение")
            ax.set_ylim(smart_ylim(exact_ys))

            # Include exact solution values in our axis determination
            all_ys = np.concatenate([all_ys, exact_ys])
            all_xs = np.concatenate([all_xs, exact_xs])

        # Show x-axis (y=0) if values are near zero
        if self._should_show_axis(all_ys):
            ax.axhline(y=0, color="k", linestyle="-", linewidth=1)

        # Show y-axis (x=0) if values are near zero
        if self._should_show_axis(all_xs):
            ax.axvline(x=0, color="k", linestyle="-", linewidth=1)

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Решение ОДУ")
        ax.grid(True)
        ax.legend()

        self.canvas.draw()
