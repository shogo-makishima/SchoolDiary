from PyQt5 import QtGui, QtCore, QtWidgets
from Scripts.Main.Settings import Settings
import Scripts.Main.StyleSheets as StyleSheets

from Scripts.Main.NetSchoolShell import Day, Lesson


class QDiaryLesson(QtWidgets.QFrame):
    def __init__(self, parent, name: str, x: int, y: int, w: int, h: int, fontSize: int = 12):
        super().__init__(parent)

        self.setObjectName(name)

        self.setGeometry(QtCore.QRect(x, y, w, h))

        self.lesson_name = QtWidgets.QLabel(self)
        self.lesson_name.setGeometry(QtCore.QRect(5, 5, w-20, 20))
        self.lesson_name.setObjectName("lesson_name")
        self.lesson_name.setStyleSheet(StyleSheets.GenerateLabelStyleSheet("lesson_name", fontSize))

        self.assignmentName = QtWidgets.QLabel(self)
        self.assignmentName.setGeometry(QtCore.QRect(10, 25, w - 20, 20))
        self.assignmentName.setObjectName("assignmentName")
        self.assignmentName.setStyleSheet(StyleSheets.GenerateLabelStyleSheet("assignmentName", fontSize - 2))

        self.setStyleSheet(StyleSheets.GenerateDiaryDayStyleSheet(name, fontSize))

    def UpdateLesson(self, lesson: Lesson):
        t_stringLesson = lesson.subjectName
        t_stringAssignment = ""
        for i in lesson.assignments:
            t_stringLesson += f" {i.mark}"
            t_stringAssignment += f"{i.assignmentName}"
        self.lesson_name.setText(t_stringLesson)
        self.assignmentName.setText(t_stringAssignment)


class QDiaryDay(QtWidgets.QFrame):
    def __init__(self, parent, name: str, x: int, y: int, w: int, h: int, fontSize: int = 15):
        super().__init__(parent)

        self.setObjectName(name)

        self.setGeometry(QtCore.QRect(x, y, w, h))

        self.day_time = QtWidgets.QLabel(self)
        self.day_time.setGeometry(QtCore.QRect(10, 10, w-20, 40))
        self.day_time.setObjectName("day_time")
        self.day_time.setStyleSheet(StyleSheets.GenerateDiaryDayStyleSheet("day_time", fontSize))

        self.lesson_1 = QDiaryLesson(self, "lesson_1", 10, 50, w-40, 50)
        self.lesson_2 = QDiaryLesson(self, "lesson_2", 10, 100, w-40, 50)
        self.lesson_3 = QDiaryLesson(self, "lesson_3", 10, 150, w-40, 50)
        self.lesson_4 = QDiaryLesson(self, "lesson_4", 10, 200, w-40, 50)
        self.lesson_5 = QDiaryLesson(self, "lesson_5", 10, 250, w-40, 50)
        self.lesson_6 = QDiaryLesson(self, "lesson_6", 10, 300, w-40, 50)
        self.lesson_7 = QDiaryLesson(self, "lesson_7", 10, 350, w-40, 50)

        self.lessons: list = [
            self.lesson_1,
            self.lesson_2,
            self.lesson_3,
            self.lesson_4,
            self.lesson_5,
            self.lesson_6,
            self.lesson_7,
        ]

        self.setStyleSheet(StyleSheets.GenerateDiaryDayStyleSheet(name, fontSize))

    def UpdateDay(self, day: Day):
        self.day_time.setText(day.date)
        for i in range(len(day.lessons)):
            self.lessons[i].UpdateLesson(day.lessons[i])


