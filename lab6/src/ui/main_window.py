from typing import Callable

from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QSplitter, QVBoxLayout, QWidget

from data import function_data
from libs.ode.methods.adams import AdamsMethod
from libs.ode.methods.core.enums import ODEMethodType
from libs.ode.methods.core.method import ODEMethod
from libs.ode.methods.euler import EulerMethod
from libs.ode.methods.runge_kutta_4_order import RungeKutta4OrderMethod
from models.function_data import FunctionData
from schemas.ode import ODERequestSchema
from ui.components.control_panel import ControlPanel
from ui.components.plot_widget import PlotWidget
from ui.components.results_table import ResultsTable
from ui.styles import DEFAULT_FONT, STYLE_SHEET
from ui.utils.alert import show_error

Function2D = Callable[[float, float], float]


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Решение ОДУ")
        self.resize(1200, 700)
        self.setup_ui()
        self.setStyleSheet(STYLE_SHEET)
        self.setFont(DEFAULT_FONT)

    def setup_ui(self) -> None:
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)

        splitter = QSplitter()

        # Left section (30%) - Control panel
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 10, 0)

        self.control_panel = ControlPanel()

        # Add functions
        for func in function_data.data:
            self.control_panel.function_selector.add_function(func)

        left_layout.addWidget(self.control_panel)

        # Right section (70%) - Plot and table
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(10, 0, 0, 0)
        right_layout.setSpacing(10)

        self.plot_widget = PlotWidget()
        self.results_table = ResultsTable()

        right_layout.addWidget(self.plot_widget, 70)
        right_layout.addWidget(self.results_table, 30)

        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)
        splitter.setSizes([300, 900])

        main_layout.addWidget(splitter)
        self.setCentralWidget(main_widget)

        self.control_panel.solve_requested.connect(self.on_solve_requested)

    def on_solve_requested(
        self,
        request: ODERequestSchema | None,
        selected_function_data: FunctionData | None,
    ) -> None:
        if request is None or selected_function_data is None:
            return

        # Validation
        if request.x0 >= request.xn:
            show_error("x0 must be less than xn")
            return

        def local_exact_solution(x: float) -> float:
            return selected_function_data.exact_solution(x, request.x0, request.y0)

        method: ODEMethod | None = None
        MAX_N = 50000
        match request.method:
            case ODEMethodType.EULER:
                method = EulerMethod(request, max_N=MAX_N)
            case ODEMethodType.RUNGE_KUTTA:
                method = RungeKutta4OrderMethod(request, max_N=MAX_N)
            case ODEMethodType.ADAMS:
                method = AdamsMethod(request, max_N=MAX_N, exact_solution=local_exact_solution)
            case _:
                show_error("Unknown method")
                return

        response = method.solve()

        self.plot_widget.plot_solution(response, local_exact_solution)
        self.results_table.update_results(response.accuracy, response.N)
