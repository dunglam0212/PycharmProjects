from PyQt6.QtWidgets import QApplication, QMainWindow

from Module7.C129TinhTienDien.MainWindowExt import MainWindowExt

app=QApplication([])
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()