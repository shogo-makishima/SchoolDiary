from Scripts.UI.Widgets.QMenu import QMenu
from PyQt5 import QtGui, QtCore, QtWidgets
from Scripts.Main.Settings import Settings, Languages
from Scripts.Main.NetSchoolShell import NetSchoolShell

from Scripts.Main.Extentions import thread

from Scripts.UI.Widgets.QDefaultButton import QDefaultButton


class MainPage(QMenu):
    name = "MainPage"

    def __init__(self, parent):
        super(MainPage, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])
        # self.menu = DefaultButton(self, "Back", 300, 200, 100, 100, "Back", lambda: parent.ChangeMenu(self.lastMenuName, isBack=True))
        self.p_loginButton = QDefaultButton(self, "Login", 60, 180, 360, 120, Languages.GetWordByKey(Languages, "Login"), lambda: self.ToLoginMenu(parent))

    def Update(self):
        pass

    @thread
    def ToLoginMenu(self, parent):
        if (NetSchoolShell.isLoginProcess): return

        if (Settings.DATA_LOGIN == None): parent.ChangeMenu("LoginPage")
        else:
            NetSchoolShell.Login(NetSchoolShell, Settings.DATA_LOGIN)
            if (NetSchoolShell.isLoginProcess): return
            if (NetSchoolShell.GetIsLogin(NetSchoolShell)): parent.ChangeMenu("DiaryPage")
