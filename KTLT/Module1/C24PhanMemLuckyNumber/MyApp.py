from PyQt6.QtWidgets import QApplication, QMainWindow

from Module1.C24PhanMemLuckyNumber.MainWindowExt import MainWindowExt

app=QApplication([])
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()