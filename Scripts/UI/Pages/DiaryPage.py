from Scripts.UI.Widgets.QMenu import QMenu
from PyQt5 import QtGui, QtCore, QtWidgets
from Scripts.Main.Settings import Settings, Languages
from Scripts.Main.NetSchoolShell import NetSchoolShell

from Scripts.Main.Extentions import thread

import datetime

from Scripts.UI.Widgets.QDefaultButton import QDefaultButton
from Scripts.UI.Widgets.QDiaryDay import QDiaryDay


class DiaryPage(QMenu):
    name = "DiaryPage"

    def __init__(self, parent):
        super(DiaryPage, self).__init__(parent)

        self.currentDayID: int = 0
        self.currentMondayDate: datetime.datetime = None

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.day_previous = QDefaultButton(self, "day_previous", 0, 180, 60, 120, Languages.GetWordByKey(Languages, "Day_Previous"), lambda: self.ChangeDay(False), fontSize=45)
        self.day_next = QDefaultButton(self, "day_next", 420, 180, 60, 120, Languages.GetWordByKey(Languages, "Day_Next"), lambda: self.ChangeDay(True), fontSize=45)

        self.day_diary = QDiaryDay(self, "day", 60, 0, 360, 480)

        self.week_previous = QDefaultButton(self, "week_previous", 0, 420, 60, 60, Languages.GetWordByKey(Languages, "Day_Previous"), lambda: self.ChangeWeek(False), fontSize=45)
        self.week_next = QDefaultButton(self, "week_next", 420, 420, 60, 60, Languages.GetWordByKey(Languages, "Day_Next"), lambda: self.ChangeWeek(True), fontSize=45)

    def ChangeWeek(self, direction: bool):
        self.currentMondayDate += datetime.timedelta(days=7) if (direction) else -datetime.timedelta(days=7)
        self.SetWeekByCurrentWeek()

    def ChangeDay(self, direction: bool):
        self.currentDayID += (1 if (direction) else -1)

        if (self.currentDayID < 0): self.currentDayID = len(NetSchoolShell.diary.weekDays) - 1
        elif (self.currentDayID >= len(NetSchoolShell.diary.weekDays)): self.currentDayID = 0

        self.SetDayByCurrentID()

    def SetDayByCurrentID(self):
        try: self.day_diary.UpdateDay(NetSchoolShell.diary.weekDays[self.currentDayID])
        except Exception as exception: print(exception)

    def SetWeekByCurrentWeek(self):
        NetSchoolShell.GetDiaryByDate(NetSchoolShell, self.currentMondayDate, self.currentMondayDate + datetime.timedelta(days=5))
        self.currentDayID = 0
        self.SetDayByCurrentID()

    def UpdateDiary(self):
        NetSchoolShell.UpdateDiary(NetSchoolShell)
        self.currentMondayDate = datetime.datetime.strptime(NetSchoolShell.diary.weekDays[0].date, '%Y-%m-%dT%H:%M:%S')
        self.SetDayByCurrentID()

    def CheckDiary(self):
        print(NetSchoolShell.diary.className)

    def Start(self):
        self.UpdateDiary()

    def Update(self):
        pass
