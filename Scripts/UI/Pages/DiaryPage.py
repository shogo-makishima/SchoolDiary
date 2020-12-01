from Scripts.UI.Widgets.QMenu import QMenu
from PyQt5 import QtGui, QtCore, QtWidgets
from Scripts.Main.Settings import Settings, Languages
from Scripts.Main.NetSchoolShell import NetSchoolShell

from Scripts.Main.Extentions import thread

from Scripts.UI.Widgets.QDefaultButton import QDefaultButton


class DiaryPage(QMenu):
    name = "DiaryPage"

    def __init__(self, parent):
        super(DiaryPage, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])
        self.p_loginButton = QDefaultButton(self, "Login", 60, 180, 360, 120, Languages.GetWordByKey(Languages, "Login"), lambda: self.CheckDiary())


    def CheckDiary(self):
        NetSchoolShell.UpdateDiary(NetSchoolShell)
        print(NetSchoolShell.diary.className)

    def Update(self):
        pass
