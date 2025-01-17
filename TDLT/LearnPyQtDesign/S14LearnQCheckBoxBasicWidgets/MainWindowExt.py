from PyQt6.QtWidgets import QMessageBox

from LearnPyQtDesign.S14LearnQCheckBoxBasicWidgets.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonSubmit.clicked.connect(self.processSubmit)
    def show(self):
        self.MainWindow.show()
    def processSubmit(self):
        str = []
        if self.checkBoxMachineLearning.isChecked() == True:
            str.append(self.checkBoxMachineLearning.text())
        if self.checkBoxDeepLeaning.isChecked() == True:
            str.append(self.checkBoxDeepLeaning.text())
        if self.checkBoxSmartContract.isChecked() == True:
            str.append(self.checkBoxSmartContract.text())
        separator = ','
        infor = 'Full Name = ' + self.fullNameLineEdit.text() + '\n'
        infor += 'Email = ' + self.emailLineEdit.text() + '\n'
        infor += 'Selected Courses:' + '\n'
        infor += separator.join(str)
        self.msg = QMessageBox()
        self.msg.setWindowTitle('Selected Courses')
        self.msg.setText(infor)

        self.msg.show()