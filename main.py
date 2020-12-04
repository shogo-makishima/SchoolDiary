import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QFontDatabase
from Scripts.UI.MainWindow import MainWindow
from Scripts.Main.NetSchoolShell import NetSchoolShell
 

app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())
