from PyQt6.QtWidgets import QApplication, QMainWindow

from Module1.C21PhanMemChinhHopToHop.MainWindowExt import MainWindowExt

app=QApplication([])
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()