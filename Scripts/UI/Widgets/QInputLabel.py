from PyQt5 import QtGui, QtCore, QtWidgets
from Scripts.Main.Settings import Settings
import Scripts.Main.StyleSheets as StyleSheets


class QInputLabel(QtWidgets.QLineEdit):
    def __init__(self, parent, name: str, x: int, y: int, w: int, h: int, text: str, fontSize: int = 15):
        super().__init__(parent)

        self.setPlaceholderText(text)

        self.setObjectName(name)

        self.setGeometry(QtCore.QRect(x, y, w, h))

        self.setStyleSheet(StyleSheets.GenerateButtonStyleSheet(name, fontSize))