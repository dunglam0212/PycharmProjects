from Module7.C127DoiFThanhC.MainWindow import Ui_MainWindow

class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonConvert.clicked.connect(self.processConvert)
    def show(self):
        self.MainWindow.show()
    def processConvert(self):
        F = float(self.lineEditF.text())
        C = (F-32)/1.8
        C = round(C,2)
        self.labelCrs.setText(str(C))
