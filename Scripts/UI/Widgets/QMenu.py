from PyQt5 import QtGui, QtCore, QtWidgets
from Scripts.Main.Settings import Settings


class QMenu(QtWidgets.QWidget):
    name = "Default"

    def __init__(self, parent, name = None):
        super(QMenu, self).__init__(parent)

        self.lastMenuName = "MainPage"

        self.parentMenu = parent
        if (name != None): self.name = name

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

    def Start(self):
        pass

    def Update(self):
        pass