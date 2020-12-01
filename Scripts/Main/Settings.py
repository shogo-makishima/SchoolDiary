import json, jsonpickle
from Scripts.Main.NetSchoolShell import DataLogin
import Scripts.Main.JsonManager as JsonManager
from Scripts.Main.NetSchoolShell import NetSchoolShell


class Settings:
    WINDOW_TITLE: str = "School Diary"
    WINDOW_SIZE: tuple = (480, 480)
    UPDATE_PAUSE: int = 10.0
    UI_PATH: str = "Sprites/UI"
    LANGUAGE: str = "ru"
    DATA_LOGIN: DataLogin = None


def Save():
    with open("save.json", "w", encoding="utf-8") as file:
        file.write(JsonManager.Serialize(Settings.DATA_LOGIN))

def Load():
    try:
        with open("save.json", "r", encoding="utf-8") as file:
            Settings.DATA_LOGIN = JsonManager.Deserialize(file.read())
            NetSchoolShell.URL = Settings.DATA_LOGIN.URL
            NetSchoolShell.Init(NetSchoolShell)
    except: pass

class Languages:
    LANGUAGE_DICT: dict = {}

    def Awake(self):
        with open("Resources/languages.json", "r", encoding="utf-8") as file:
            self.LANGUAGE_DICT = json.load(file)

    def GetWordByKey(self, key) -> str:
        t_string: str = ""
        try: t_string = self.LANGUAGE_DICT[key][Settings.LANGUAGE]
        except: return "Unknown"
        return t_string
