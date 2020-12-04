from netschoolapi import NetSchoolAPI, LoginForm
import datetime, trio, threading, asyncio, requests, json

def thread(func):

    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()

    return wrapper


class Assigment:

    def __init__(self):
        self.mark = ''
        self.id = 26031467
        self.typeId = 3
        self.assignmentName = 'п.1-12'
        self.weight = 0
        self.dueDate = '2020-10-19T00:00:00'
        self.classMeetingId = 29431728


class Lesson:

    def __init__(self):
        self.classmeetingId = 0
        self.day = ''
        self.number = 0
        self.room = None
        self.startTime = ''
        self.endTime = ''
        self.subjectName = ''
        self.assignments = []


class Day:

    def __init__(self):
        self.date = '2020-10-19T00:00:00'
        self.lessons = []


class Diary:

    def __init__(self):
        self.weekDays = []
        self.termName = '1 четверть'
        self.className = '8а'


class PrepareData:

    def __init__(self, id: int, name: str):
        self.id, self.name = id, name


class DataLogin:
    URL = ''
    LOGIN = ''
    PASSWORD = ''
    COUNTRY = 'Россия'
    STATE = ''
    FUNC = ''
    CITY = ''
    PROVINCE = ''
    SCHOOL = ''

    def __init__(self, url, login, password, state, func, city, province, school):
        self.URL, self.LOGIN, self.PASSWORD, self.STATE, self.FUNC, self.CITY, self.PROVINCE, self.SCHOOL = (
         url, login, password, state, func, city, province, school)


class NetSchoolShell:
    URL = ''
    URL: str
    DATA = {}
    DATA: dict
    diary = ()
    diary: Diary
    lastDateRequest = datetime.datetime.now()
    isLoginProcess = False
    isLoginProcess: bool

    def Init(self):
        try:
            self._NetSchoolShell__api = NetSchoolAPI(self.URL)
        except Exception as exception:
            try:
                print(exception)
            finally:
                exception = None
                del exception

    def UpdateLoginData(self) -> None:
        self.DATA = {}
        response = requests.get(self.URL + '/webapi/prepareloginform')
        d_data = response.json()
        for key in d_data.keys():
            if type(d_data[key]) == list:
                for data in d_data[key]:
                    if self.DATA.get(key):
                        self.DATA[key].append(PrepareData(data['id'], data['name']))
                    else:
                        self.DATA[key] = [
                         PrepareData(data['id'], data['name'])]

    def GetStringListByKey(self, key) -> list:
        t_list = list()
        for i in self.DATA[key]:
            t_list.append(i.name)
        else:
            return t_list

    def Login(self, data: DataLogin):
        self.isLoginProcess = True
        try:
            trio.run(lambda : self._NetSchoolShell__api.login(login=(data.LOGIN), password=(data.PASSWORD), country=(data.COUNTRY), func=(data.FUNC), city=(data.CITY), state=(data.STATE), province=(data.PROVINCE), school=(data.SCHOOL)))
        except Exception as exception:
            try:
                print(exception)
            finally:
                exception = None
                del exception

        else:
            self.isLoginProcess = False

    def GetIsLogin(self) -> bool:
        return self._NetSchoolShell__api.logged_in

    def UpdateDiary(self) -> None:
        dictDiary = trio.run(lambda : self._NetSchoolShell__api.get_diary())
        self.ParseDiary(self, dictDiary)

    def GetDiaryByDate(self, weekStart: datetime.datetime, weekEnd: datetime.datetime=None):
        dictDiary = trio.run(lambda : self._NetSchoolShell__api.get_diary(weekStart, weekEnd))
        self.ParseDiary(self, dictDiary)

    def ParseDiary(self, dictDiary: dict):
        self.diary = Diary()
        self.diary.termName = dictDiary['termName']
        self.diary.className = dictDiary['className']
        for day in dictDiary['weekDays']:
            newDay = Day()
            newDay.date = day['date']
            for lesson in day['lessons']:
                newLesson = Lesson()
                newLesson.classmeetingId = lesson['classmeetingId']
                newLesson.day = lesson['day']
                newLesson.number = lesson['number']
                newLesson.room = lesson['room']
                newLesson.endTime = lesson['endTime']
                newLesson.startTime = lesson['startTime']
                newLesson.subjectName = lesson['subjectName']
                if lesson.get('assignments'):
                    for assigment in lesson['assignments']:
                        newAssigment = Assigment()
                        newAssigment.id = assigment['id']
                        if assigment['mark'] != None:
                            newAssigment.mark = assigment['mark']['mark']
                        newAssigment.typeId = assigment['typeId']
                        newAssigment.weight = assigment['weight']
                        newAssigment.assignmentName = assigment['assignmentName']
                        newAssigment.classMeetingId = assigment['classMeetingId']
                        newAssigment.dueDate = assigment['dueDate']
                        newLesson.assignments.append(newAssigment)

                else:
                    newDay.lessons.append(newLesson)
            else:
                self.diary.weekDays.append(newDay)

    def Logout(self):
        trio.run(lambda : self._NetSchoolShell__api.logout())