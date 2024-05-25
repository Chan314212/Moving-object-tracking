from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
                               QWidget)
from Ui_main import Ui_MainWindow


def setBut(but: QPushButton):
    but.setStyleSheet(
        "QPushButton{font-size: 13pt;background-color: #9bc2df;border-radius:10px;padding:2px 4px;border-style: outset;}"
        "QPushButton:hover{background-color:#b1deff; color: black;}"
        "QPushButton:pressed{background-color:#b1deff;border-style: inset;}"
    )


def setButs(buts):
    for but in buts:
        setBut(but)
