from Scripts.UI.Widgets.QMenu import QMenu
from PyQt5 import QtGui, QtCore, QtWidgets
from Scripts.Main.Settings import Settings, Languages
from Scripts.Main.NetSchoolShell import NetSchoolShell

from Scripts.Main.Extentions import thread

from Scripts.UI.Widgets.QDefaultButton import QDefaultButton
from Scripts.UI.Widgets.QDiaryDay import QDiaryDay


class DiaryPage(QMenu):
    name = "DiaryPage"

    def __init__(self, parent):
        super(DiaryPage, self).__init__(parent)

        self.currentDayID: int = 0

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.day_previous = QDefaultButton(self, "day_previous", 0, 180, 60, 120, Languages.GetWordByKey(Languages, "Day_Previous"), lambda: self.ChangeDay(False), fontSize=45)
        self.day_next = QDefaultButton(self, "day_next", 420, 180, 60, 120, Languages.GetWordByKey(Languages, "Day_Next"), lambda: self.ChangeDay(True), fontSize=45)

        self.day_diary = QDiaryDay(self, "day", 60, 0, 360, 480)

    def ChangeDay(self, direction: bool):
        self.currentDayID += (1 if (direction) else -1)

        if (self.currentDayID < 0): self.currentDayID = len(NetSchoolShell.diary.weekDays) - 1
        elif (self.currentDayID >= len(NetSchoolShell.diary.weekDays)): self.currentDayID = 0

        self.SetDayByCurrentID()

    def SetDayByCurrentID(self):
        print(NetSchoolShell.diary.weekDays)
        self.day_diary.UpdateDay(NetSchoolShell.diary.weekDays[self.currentDayID])

    def UpdateDiary(self):
        NetSchoolShell.UpdateDiary(NetSchoolShell)
        self.SetDayByCurrentID()

    def CheckDiary(self):
        print(NetSchoolShell.diary.className)

    def Start(self):
        self.UpdateDiary()

    def Update(self):
        pass
