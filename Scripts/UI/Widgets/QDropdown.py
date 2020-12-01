from PyQt5 import QtGui, QtCore, QtWidgets
from Scripts.Main.Settings import Settings
import Scripts.Main.StyleSheets as StyleSheets


class QDropdown(QtWidgets.QComboBox):
    def __init__(self, parent, name: str, x: int, y: int, w: int, h: int, fontSize: int = 15):
        super().__init__(parent)

        self.setObjectName(name)

        self.setGeometry(QtCore.QRect(x, y, w, h))

        self.setStyleSheet(StyleSheets.GenerateDropDownStyleSheet(name, fontSize))

        self.addItems(["None"])

    def UpdateItems(self, items: list):
        self.clear()
        self.addItems(items)