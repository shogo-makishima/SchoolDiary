from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import threading, time, sqlite3
from Scripts.UI.Widgets.QMenu import QMenu

from Scripts.Main.NetSchoolShell import NetSchoolShell
from Scripts.Main.Settings import Settings, Languages, Load

from Scripts.UI.Pages.MainPage import MainPage
from Scripts.UI.Pages.LoginPage import LoginPage
from Scripts.UI.Pages.DiaryPage import DiaryPage


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        Load()
        NetSchoolShell.Init(NetSchoolShell)

        self.Start()

        super().__init__()

        self.ListMenus: tuple = (
            QMenu(self),
            MainPage(self),
            LoginPage(self),
            DiaryPage(self),
        )

        self.setWindowTitle(Settings.WINDOW_TITLE)

        self.setObjectName("Menu")
        self.setGeometry(100, 100, Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.currentMenu: QMenu = self.GetMenuByName("MainPage")
        print(f"[MENU][CURRENT] {self.currentMenu.name}")

        self.timer = QtCore.QTimer(self)
        self.timer.start(Settings.UPDATE_PAUSE)
        self.timer.timeout.connect(lambda: self.UpdateChildMenu())

        self.setStyleSheet("background-color: black;")
        self.Update()

    def Start(self):
        Languages.Awake(Languages)
        self.UpdateState()

    def UpdateState(self):
        pass

    def UpdateChildMenu(self):
        self.UpdateState()
        self.currentMenu.Update()

    def Update(self):
        for menu in self.ListMenus:
            menu.setHidden(not (menu == self.currentMenu))

        self.show()

    def ChangeMenu(self, name: str = "Menu", parameter: bool = True, isBack = False):
        if (parameter):
            t_lastMenuName = self.currentMenu.name
            # print(self.currentMenu.lastMenuName)
            self.currentMenu: QMenu = self.GetMenuByName(name)
            print(f"[MENU][CURRENT] {self.currentMenu.name}")

            self.currentMenu.Start()
            self.Update()

            if (not isBack):
                self.currentMenu.lastMenuName = t_lastMenuName

    def GetMenuByName(self, name: str = "Default") -> QMenu:
        for menu in self.ListMenus:
            if (menu.name == name): return menu

        for menu in self.ListMenus:
            if (menu.name == "Default"): return menu