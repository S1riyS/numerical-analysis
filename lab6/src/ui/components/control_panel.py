from typing import Callable

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget

from models.function_data import FunctionData
from schemas.ode import ODERequestSchema
from ui.components.function_selector import FunctionSelector
from ui.components.method_selector import MethodSelector
from ui.components.numeric_input import NumericInput
from ui.utils.alert import show_error

Function2D = Callable[[float, float], float]


class ControlPanel(QWidget):
    solve_requested = pyqtSignal(ODERequestSchema, FunctionData)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        # Numeric inputs
        self.x0_input = NumericInput("Начало отрезка", "x₀", 0.0, -100, 100)
        self.xn_input = NumericInput("Конец отрезка", " xₙ", 1.0, -100, 100)
        self.y0_input = NumericInput("Начальное значение", "y₀", 1.0, -100, 100)
        self.n_input = NumericInput("Начальное количество точек", "N", 8, 5, 1000)
        self.eps_input = NumericInput("Точность", "ε", 0.001, 1e-6, 1)

        self.numeric_inputs = [
            self.x0_input,
            self.xn_input,
            self.y0_input,
            self.n_input,
            self.eps_input,
        ]

        # Function selector
        self.function_selector = FunctionSelector()

        # Method selector
        self.method_selector = MethodSelector()

        # Solve button
        self.solve_button = QPushButton("Решить")

        # Add widgets to layout
        layout.addWidget(self.x0_input)
        layout.addWidget(self.xn_input)
        layout.addWidget(self.y0_input)
        layout.addWidget(self.n_input)
        layout.addWidget(self.eps_input)
        layout.addWidget(self.function_selector)
        layout.addWidget(self.method_selector)
        layout.addStretch()
        layout.addWidget(self.solve_button)

    def setup_connections(self) -> None:
        self.solve_button.clicked.connect(self.on_solve_clicked)

    def on_solve_clicked(self) -> None:
        if not all(input_field.validate_input() for input_field in self.numeric_inputs):
            show_error("Invalid input")
            return

        try:
            function_data = self.function_selector.get_current_function()
            request = ODERequestSchema(
                x0=self.x0_input.get_value(),
                xn=self.xn_input.get_value(),
                y0=self.y0_input.get_value(),
                f=function_data.func,
                N=int(self.n_input.get_value()),
                eps=self.eps_input.get_value(),
                method=self.method_selector.get_current_method(),
            )

            self.solve_requested.emit(request, function_data)

        except ValueError as e:
            print(f"Invalid input: {e}")
