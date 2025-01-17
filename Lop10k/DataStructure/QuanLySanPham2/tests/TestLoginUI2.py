from PyQt6.QtWidgets import QApplication, QMainWindow

from DataStructure.QuanLySanPham2.ui.MainWindowLoginExt import MainWindowLoginExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowLoginExt()
myui.setupUi(mainwindow)
#test show window 2
myui.show()
app.exec()