from PyQt6.QtWidgets import QApplication, QMainWindow

from LearnPyQtDesign.S49MySQLPart1.MainWindowExt import MainWindowExt

app = QApplication([])
myWindow = MainWindowExt()
myWindow.setupUi(QMainWindow())
#myWindow.connectMySQL()
myWindow.selectAllStudent()
myWindow.show()
app.exec()
