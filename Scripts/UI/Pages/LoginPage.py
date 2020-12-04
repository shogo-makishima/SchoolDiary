from Scripts.UI.Widgets.QMenu import QMenu
from PyQt5 import QtGui, QtCore, QtWidgets
from Scripts.Main.Settings import Settings, Languages, Save

from Scripts.Main.Extentions import thread

from Scripts.Main.NetSchoolShell import NetSchoolShell, DataLogin

from Scripts.UI.Widgets.QDefaultButton import QDefaultButton
from Scripts.UI.Widgets.QInputLabel import QInputLabel
from Scripts.UI.Widgets.QDropdown import QDropdown


class LoginPage(QMenu):
    name = "LoginPage"

    def __init__(self, parent):
        super(LoginPage, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.p_loginButton = QDefaultButton(self, "login", 0, 450, 480, 30, Languages.GetWordByKey(Languages, "Login"), lambda: self.LoginPress(parent), fontSize=10)

        self.url_input = QInputLabel(self, "url_input", 0, 0, 480, 30, Languages.GetWordByKey(Languages, "Input_URL"), fontSize=10)
        self.b_getUrlDataButton = QDefaultButton(self, "url_data", 0, 30, 480, 30, Languages.GetWordByKey(Languages, "Update_URL"), lambda: self.GetUrlData(), fontSize=10)

        self.s_countriesDropdown = QDropdown(self, "countries_drop", 0, 90, 480, 30, fontSize=10)
        self.s_citiesDropdown = QDropdown(self, "cities_drop", 0, 120, 480, 30, fontSize=10)
        self.s_statesDropdown = QDropdown(self, "states_drop", 0, 150, 480, 30, fontSize=10)
        self.s_provincesDropdown = QDropdown(self, "provinces_drop", 0, 180, 480, 30, fontSize=10)
        self.s_funcsDropdown = QDropdown(self, "funcs_drop", 0, 210, 480, 30, fontSize=10)
        self.s_schoolsDropdown = QDropdown(self, "schools_drop", 0, 240, 480, 30, fontSize=10)

        self.login_input = QInputLabel(self, "login_input", 0, 270, 480, 30, Languages.GetWordByKey(Languages, "Input_Login"), fontSize=10)
        self.password_input = QInputLabel(self, "password_input", 0, 300, 480, 30, Languages.GetWordByKey(Languages, "Input_Password"), fontSize=10)


    def Update(self):
        pass

    @thread
    def GetUrlData(self):
        try:
            NetSchoolShell.URL = self.url_input.text()
            NetSchoolShell.Init(NetSchoolShell)
            NetSchoolShell.UpdateLoginData(NetSchoolShell)

            self.s_countriesDropdown.UpdateItems(NetSchoolShell.GetStringListByKey(NetSchoolShell, "countries"))
            self.s_citiesDropdown.UpdateItems(NetSchoolShell.GetStringListByKey(NetSchoolShell, "cities"))
            self.s_statesDropdown.UpdateItems(NetSchoolShell.GetStringListByKey(NetSchoolShell, "states"))
            self.s_provincesDropdown.UpdateItems(NetSchoolShell.GetStringListByKey(NetSchoolShell, "provinces"))
            self.s_funcsDropdown.UpdateItems(NetSchoolShell.GetStringListByKey(NetSchoolShell, "funcs"))
            self.s_schoolsDropdown.UpdateItems(NetSchoolShell.GetStringListByKey(NetSchoolShell, "schools"))

            # https://edu.admoblkaluga.ru:444
        except Exception as exception: print(exception)

    @thread
    def LoginPress(self, parent):
        if (NetSchoolShell.isLoginProcess): return

        if (Settings.DATA_LOGIN == None):
            url = self.url_input.text()
            city = self.s_citiesDropdown.currentText()
            state = self.s_statesDropdown.currentText()
            province = self.s_provincesDropdown.currentText()
            func = self.s_funcsDropdown.currentText()
            school = self.s_schoolsDropdown.currentText()
            login = self.login_input.text()
            password = self.password_input.text()

            Settings.DATA_LOGIN = DataLogin(url, login, password, state, func, city, province, school)

        NetSchoolShell.Login(NetSchoolShell, Settings.DATA_LOGIN)
        if (NetSchoolShell.GetIsLogin(NetSchoolShell)):
            Save()
            parent.ChangeMenu("DiaryPage")