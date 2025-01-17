from Module7.C138Calculator.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton0.clicked.connect(self.process0)
        self.pushButton1.clicked.connect(self.process1)
        self.pushButton2.clicked.connect(self.process2)
        self.pushButton3.clicked.connect(self.process3)
        self.pushButton4.clicked.connect(self.process4)
        self.pushButton5.clicked.connect(self.process5)
        self.pushButton6.clicked.connect(self.process6)
        self.pushButton7.clicked.connect(self.process7)
        self.pushButton8.clicked.connect(self.process8)
        self.pushButton9.clicked.connect(self.process9)
        self.pushButtonCommonDot.clicked.connect(self.processdot)
        self.pushButtonClear.clicked.connect(self.processClear)
        self.pushButtonPlus.clicked.connect(self.processPlus)
    def show(self):
        self.MainWindow.show()
    def process0(self):
        self.labelResult.setText(self.labelResult.text() + '0')
    def process1(self):
        self.labelResult.setText(self.labelResult.text() +'1')
    def process2(self):
        self.labelResult.setText(self.labelResult.text() +'2')
    def process3(self):
        self.labelResult.setText(self.labelResult.text() +'3')
    def process4(self):
        self.labelResult.setText(self.labelResult.text() +'4')
    def process5(self):
        self.labelResult.setText(self.labelResult.text() +'5')
    def process6(self):
        self.labelResult.setText(self.labelResult.text() +'6')
    def process7(self):
        self.labelResult.setText(self.labelResult.text() +'7')
    def process8(self):
        self.labelResult.setText(self.labelResult.text() +'8')
    def process9(self):
        self.labelResult.setText(self.labelResult.text() +'9')
    def processdot(self):
        self.labelResult.setText(self.labelResult.text() + '.')
    def processClear(self):
        self.labelResult.setText('')

