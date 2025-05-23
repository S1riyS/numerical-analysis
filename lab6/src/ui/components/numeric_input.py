from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget


class NumericInput(QWidget):
    value_changed = pyqtSignal(float)

    def __init__(
        self,
        label: str,
        variable: str,
        default: float = 0.0,
        min_val: float = -float("inf"),
        max_val: float = float("inf"),
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.min_val = min_val
        self.max_val = max_val
        self.setup_ui(label, variable, default)

    def setup_ui(self, label: str, variable: str, default: float) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)  # Add some spacing between label and input

        self.label = QLabel(f"{label} ({variable} ∈ [{self.min_val}, {self.max_val}]):")
        self.input = QLineEdit()

        validator = QDoubleValidator()
        validator.setBottom(self.min_val)
        validator.setTop(self.max_val)
        self.input.setValidator(validator)

        self.input.setText(str(default))
        self.input.textEdited.connect(self.validate_input)

        layout.addWidget(self.label)
        layout.addWidget(self.input)

    def validate_input(self) -> bool:
        try:
            value = float(self.input.text().replace(",", "."))
            if value < self.min_val or value > self.max_val:
                raise ValueError
            self.value_changed.emit(value)
        except ValueError:
            self.input.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.input.setStyleSheet("")
            return True

    def get_value(self) -> float:
        return float(self.input.text().replace(",", "."))
