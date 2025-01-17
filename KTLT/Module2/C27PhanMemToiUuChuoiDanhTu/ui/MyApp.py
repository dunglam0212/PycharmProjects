from PyQt6.QtWidgets import QApplication, QMainWindow

from Module2.C27PhanMemToiUuChuoiDanhTu.ui.MainWindowExt import MainWindowExt

app=QApplication([])
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()