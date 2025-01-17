from LearnPyQtDesign.S16LearnQComboxAdvanced.Employee import Employee
from LearnPyQtDesign.S16LearnQComboxAdvanced.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonClose.clicked.connect(self.processClose)
        self.pushButtonConfirm.clicked.connect(self.processConfirm)
    def show(self):
        self.MainWindow.show()
    def processClose(self):
        self.MainWindow.close()
    def processConfirm(self):
        name = self.labelFullname.text()
        gender = 'Male'
        if self.checkBoxFemale.isChecked():
            gender='Female'
        city = self.comboBoxCity.currentText()
        emp = Employee(name, gender, city)
        self.plainTextEditOutput.setPlainText(str(emp))
