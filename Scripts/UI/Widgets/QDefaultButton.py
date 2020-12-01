from PyQt5 import QtGui, QtCore, QtWidgets
from Scripts.Main.Settings import Settings
import Scripts.Main.StyleSheets as StyleSheets


class QDefaultButton(QtWidgets.QPushButton):
    def __init__(self, parent, name: str, x: int, y: int, w: int, h: int, text: str, func, fontSize: int = 15, isButton: bool = True):
        super().__init__(parent)

        self.setText(text)

        self.setObjectName(name)

        if (isButton): self.clicked.connect(func)
        self.setEnabled(isButton)

        self.setGeometry(QtCore.QRect(x, y, w, h))

        self.setStyleSheet(StyleSheets.GenerateButtonStyleSheet(name, fontSize))