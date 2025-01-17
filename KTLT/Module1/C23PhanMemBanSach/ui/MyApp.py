from PyQt6.QtWidgets import QApplication, QMainWindow

from Module1.C23PhanMemBanSach.ui.MainWindowExt import MainWindowExt

app=QApplication([])
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
myWindow.processNhapThongTin()
app.exec()