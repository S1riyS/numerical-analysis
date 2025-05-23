from typing import Dict

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget

from models.function_data import FunctionData


class FunctionSelector(QWidget):
    function_changed = pyqtSignal(FunctionData)  # Emits Function2D

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.functions: Dict[str, FunctionData] = {}
        self.setup_ui()

    def setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel("Функция:")
        self.combo = QComboBox()

        layout.addWidget(self.label)
        layout.addWidget(self.combo)

        self.combo.currentIndexChanged.connect(self.on_function_changed)

    def add_function(self, data: FunctionData) -> None:
        processed_expr = f"f'(x, y) = {data.str_expr}"
        self.functions[processed_expr] = data
        self.combo.addItem(processed_expr)

        if len(self.functions) == 1:
            self.combo.setCurrentIndex(0)

    def on_function_changed(self, index: int) -> None:
        func_name = self.combo.currentText()
        self.function_changed.emit(self.functions[func_name])

    def get_current_function(self) -> FunctionData:
        return self.functions[self.combo.currentText()]
