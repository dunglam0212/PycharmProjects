from PyQt6.QtWidgets import QApplication, QMainWindow

from Module2.C33PhanMemTuongTacMang.ui.MainWindowExt import MainWindowExt

app=QApplication([])
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()