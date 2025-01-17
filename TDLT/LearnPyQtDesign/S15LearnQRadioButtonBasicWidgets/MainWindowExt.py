from PyQt6.QtWidgets import QMessageBox
from debugpy.common import json

from LearnPyQtDesign.S15LearnQRadioButtonBasicWidgets.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonSendData.clicked.connect(self.processSendData)
    def show(self):
        self.MainWindow.show()
    def processSendData(self):
        fullname = self.fullNameLineEdit.text()
        email = self.emailLineEdit.text()
        gender = 'Female'
        if not self.radioButtonFemale.isChecked():
            gender = self.radioButton_Male.text()
        address = self.lineEditAddress.text()
        education = 'Bachelor'
        if self.radioButtonMaster.isChecked():
            education = self.radioButtonMaster.text()
        elif self.radioButtonDoctoral.isChecked():
            education = self.radioButtonDoctoral.text()
        information = {'Fullname':fullname,
                       'Email':email,
                       'Gender':gender,
                       'Address':address,
                       'Education':education,
                       }
        self.msgBox = QMessageBox()
        self.msgBox.setWindowTitle('Information')
        self.msgBox.setText(json.dumps(information, ensure_ascii=False))
        self.msgBox.show()
