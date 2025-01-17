from PyQt6.QtWidgets import QMessageBox

from CalculateWithFractions.process.Fraction import add_fractions, substract_fractions, multiple_fractions, \
    divide_fractions
from CalculateWithFractions.ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
        self.calculate_choice = ""
        self.fraction1 = ""
        self.fraction2 = ""
        self.lineEditInputText = ""
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonExit.clicked.connect(self.processExit)
        self.pushButtonNew.clicked.connect(self.processNew)
        self.pushButton1.clicked.connect(self.process1)
        self.pushButton2.clicked.connect(self.process2)
        self.pushButton3.clicked.connect(self.process3)
        self.pushButton4.clicked.connect(self.process4)
        self.pushButton5.clicked.connect(self.process5)
        self.pushButton6.clicked.connect(self.process6)
        self.pushButton7.clicked.connect(self.process7)
        self.pushButton8.clicked.connect(self.process8)
        self.pushButton9.clicked.connect(self.process9)
        self.pushButtonAdd.clicked.connect(self.processAdd)
        self.pushButtonSubstract.clicked.connect(self.processSubstract)
        self.pushButtonMultiple.clicked.connect(self.processMultiple)
        self.pushButtonDivide.clicked.connect(self.processDivide)
        self.pushButtonFraction.clicked.connect(self.processFraction)
        self.pushButtonEqual.clicked.connect(self.processEqual)
    def processExit(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Xác nhận thoát')
        msgBox.setText('Bạn có chắc chắn muốn thoát không?')
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes |
                                  QMessageBox.StandardButton.No)
        rs = msgBox.exec()
        if rs == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
    def processNew(self):
        self.lineEditInput.setText('')
        self.lineEditResult.setText('')
        self.lineEditInputText = ""
    def process1(self):
        self.lineEditInputText = self.lineEditInputText + "1"
        self.lineEditInput.setText(self.lineEditInputText)
    def process2(self):
        self.lineEditInputText = self.lineEditInputText + "2"
        self.lineEditInput.setText(self.lineEditInputText)
    def process3(self):
        self.lineEditInputText = self.lineEditInputText + "3"
        self.lineEditInput.setText(self.lineEditInputText)
    def process4(self):
        self.lineEditInputText = self.lineEditInputText + "4"
        self.lineEditInput.setText(self.lineEditInputText)
    def process5(self):
        self.lineEditInputText = self.lineEditInputText + "5"
        self.lineEditInput.setText(self.lineEditInputText)
    def process6(self):
        self.lineEditInputText = self.lineEditInputText + "6"
        self.lineEditInput.setText(self.lineEditInputText)
    def process7(self):
        self.lineEditInputText = self.lineEditInputText + "7"
        self.lineEditInput.setText(self.lineEditInputText)
    def process8(self):
        self.lineEditInputText = self.lineEditInputText + "8"
        self.lineEditInput.setText(self.lineEditInputText)
    def process9(self):
        self.lineEditInputText = self.lineEditInputText + "9"
        self.lineEditInput.setText(self.lineEditInputText)
    def processAdd(self):
        self.lineEditInputText = self.lineEditInputText + " + "
        self.lineEditInput.setText(self.lineEditInputText)
    def processSubstract(self):
        self.lineEditInputText = self.lineEditInputText + " - "
        self.lineEditInput.setText(self.lineEditInputText)
    def processMultiple(self):
        self.lineEditInputText = self.lineEditInputText + " × "
        self.lineEditInput.setText(self.lineEditInputText)
    def processDivide(self):
        self.lineEditInputText = self.lineEditInputText + " ÷ "
        self.lineEditInput.setText(self.lineEditInputText)
    def processFraction(self):
        self.lineEditInputText = self.lineEditInputText + "/"
        self.lineEditInput.setText(self.lineEditInputText)
    def print_warning_message(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Warning")
        msgBox.setText("Valid Error!")
        msgBox.setInformativeText("Please enter again!")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.setIcon(QMessageBox.Icon.Warning)
        msgBox.exec()
        self.processNew()
    def processEqual(self):
        try:
            split = self.lineEditInputText.split(" ")
            if len(split) != 3:
                self.print_warning_message()
                return
            else:
                f1 = split[0]
                f2 = split[2]
                if split[1] == "+":
                    rs = add_fractions(f1,f2)
                    if rs == False:
                        self.print_warning_message()
                        return
                    else:
                        self.lineEditResult.setText(rs)
                elif split[1] == "-":
                    rs = substract_fractions(f1,f2)
                    if rs == False:
                        self.print_warning_message()
                        return
                    else:
                        self.lineEditResult.setText(rs)
                elif split[1] == "×":
                    rs = multiple_fractions(f1,f2)
                    if rs == False:
                        self.print_warning_message()
                        return
                    else:
                        self.lineEditResult.setText(rs)
                elif split[1] == "÷":
                    rs = divide_fractions(f1,f2)
                    if rs == False:
                        self.print_warning_message()
                        return
                    else:
                        self.lineEditResult.setText(rs)
                else:
                    self.print_warning_message()
                    return
        except:
            self.print_warning_message()
            return