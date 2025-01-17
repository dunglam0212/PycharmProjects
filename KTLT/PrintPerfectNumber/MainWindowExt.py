from PyQt6.QtWidgets import QMainWindow

from PrintPerfectNumber.MainWindow import Ui_MainWindow
from PrintPerfectNumber.ProcessPrintPerfectNumbers import print_perfect_numbers_from_1_to_N
from PrintPerfectNumber.ResultWindowExt import ResultWindowExt


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonPrint.clicked.connect(self.processPrint)
    def processPrint(self):
        self.resultwindow = QMainWindow()
        self.resultUi = ResultWindowExt()
        self.resultUi.setupUi(self.resultwindow)
        self.resultUi.show()
        n = int(self.lineEditN.text())
        if n>0:
            rs = print_perfect_numbers_from_1_to_N(n)
            if rs == []:
                pass