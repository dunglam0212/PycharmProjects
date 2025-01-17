from PyQt6.QtWidgets import QApplication, QMainWindow

from LearnPyQtDesign.S14LearnQCheckBoxBasicWidgets.MainWindowExt import MainWindowExt

app=QApplication([])
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()