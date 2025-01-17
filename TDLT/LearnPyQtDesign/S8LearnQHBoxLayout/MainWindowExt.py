from LearnPyQtDesign.S8LearnQHBoxLayout.MainWindowFirstDegreeEquation import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.MainWindow.setWindowTitle("First Degree Equation")
        self.pushButtonSolution.clicked.connect(self.processSolution)
        self.pushButtonClear.clicked.connect(self.processClear)
        self.pushButtonExit.clicked.connect(self.processExit)
    def show(self):
        self.MainWindow.show()
    def processSolution(self):
        a = float(self.lineEdita.text())
        b = float(self.lineEditb.text())
        if a==0 and b==0:
            self.lineEditSolution.setText('Infinities Solutions')
        elif a==0 and b!=0:
            self.lineEditSolution.setText('No Solution')
        else:
            self.lineEditSolution.setText('X = ' + str(-b/a))
    def processClear(self):
        self.lineEdita.setText('')
        self.lineEditb.setText('')
        self.lineEditSolution.setText('')
        self.lineEdita.setFocus()
    def processExit(self):
        self.MainWindow.close()

