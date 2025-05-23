from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget

from libs.ode.methods.core.enums import ODEMethodType


class MethodSelector(QWidget):
    method_changed = pyqtSignal(ODEMethodType)

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel("Метод решения:")
        self.combo = QComboBox()

        # Add all available methods
        for method in ODEMethodType:
            self.combo.addItem(method.value)

        layout.addWidget(self.label)
        layout.addWidget(self.combo)

        self.combo.currentTextChanged.connect(self.on_method_changed)

    def on_method_changed(self, method_name: str) -> None:
        self.method_changed.emit(ODEMethodType(method_name))

    def get_current_method(self) -> ODEMethodType:
        return ODEMethodType(self.combo.currentText())
