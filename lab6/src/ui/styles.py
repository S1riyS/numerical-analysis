from PyQt5.QtGui import QFont

DEFAULT_FONT = QFont("Arial", 10)
HEADER_FONT = QFont("Arial", 12, QFont.Bold)

STYLE_SHEET = """
    QWidget {
        font-family: Arial;
    }
    QLineEdit {
        padding: 5px;
        border: 1px solid #ccc;
        border-radius: 3px;
    }
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QTableWidget {
        border: 1px solid #ddd;
    }
    QHeaderView::section {
        background-color: #f2f2f2;
        padding: 5px;
    }
    
    /* QMessageBox styling */
    QMessageBox {
        background-color: #f8f9fa;
    }
    QMessageBox QLabel {
        color: #212529;
        font-size: 10pt;
    }
    QMessageBox QPushButton {
        background-color: #6c757d;
        color: white;
        min-width: 80px;
    }
    QMessageBox QPushButton:hover {
        background-color: #5a6268;
    }
    QMessageBox QPushButton#okButton {
        background-color: #28a745;
    }
    QMessageBox QPushButton#okButton:hover {
        background-color: #218838;
    }
    QMessageBox QPushButton#cancelButton {
        background-color: #dc3545;
    }
    QMessageBox QPushButton#cancelButton:hover {
        background-color: #c82333;
    }
"""
