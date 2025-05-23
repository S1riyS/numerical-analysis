from PyQt5.QtWidgets import (
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class ResultsTable(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Достигнутая точность", "Количество точек"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

    def update_results(self, accuracy: float, point_count: int) -> None:
        self.table.setRowCount(1)

        accuracy_item = QTableWidgetItem(f"{accuracy:.10f}")
        point_count_item = QTableWidgetItem(str(point_count))

        self.table.setItem(0, 0, accuracy_item)
        self.table.setItem(0, 1, point_count_item)
