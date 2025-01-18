from PyQt6.QtWidgets import QApplication, QMainWindow

from Module2.InvoiceManagement.ui.MainWindowExt import MainWindowExt

app = QApplication([])
mywindow = MainWindowExt()
mywindow.setupUi(QMainWindow())
mywindow.show()
app.exec()