from PyQt6.QtWidgets import QApplication, QMainWindow

from LearnPyQtDesign.S26LearnModelViewPart1.MainWindowExt import MainWindowExt

app=QApplication([])
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()