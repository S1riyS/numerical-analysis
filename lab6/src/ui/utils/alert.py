from PyQt5.QtWidgets import QMessageBox

from ui.styles import STYLE_SHEET


def show_error(message: str) -> None:
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setStyleSheet(STYLE_SHEET)  # Apply the stylesheet

    # setting message for Message Box
    msg.setText(message)

    # setting Message box window title
    msg.setWindowTitle("Error")

    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok)

    # Set object names for styling specific buttons
    ok_button = msg.button(QMessageBox.Ok)
    ok_button.setObjectName("okButton")

    # start the app
    msg.exec_()
