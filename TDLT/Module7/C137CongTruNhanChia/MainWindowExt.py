from PyQt6.QtGui import QMoveEvent
from PyQt6.QtWidgets import QMessageBox

from Module7.C137CongTruNhanChia.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonThoat.clicked.connect(self.processThoat)
        self.pushButtonCong.clicked.connect(self.processCong)
        self.pushButtonTru.clicked.connect(self.processTru)
        self.pushButtonNhan.clicked.connect(self.processNhan)
        self.pushButtonChia.clicked.connect(self.processChia)
    def show(self):
        self.MainWindow.show()
    def processThoat(self):
        dlg = QMessageBox()
        dlg.setWindowTitle('Exit Information')
        dlg.setText('Do you want to exit?')
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes|
                               QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
        else:
            pass
    def processCong(self):
        try:
            a = float(self.sALineEdit.text())
            b = float(self.sBLineEdit.text())
            self.kTQuLineEdit.setText(str(b+a))
        except:
            dlg = QMessageBox()
            dlg.setWindowTitle('Warning')
            dlg.setText('Value Error')
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
    def processTru(self):
        try:
            a = float(self.sALineEdit.text())
            b = float(self.sBLineEdit.text())
            self.kTQuLineEdit.setText(str(b-a))
        except:
            dlg = QMessageBox()
            dlg.setWindowTitle('Warning')
            dlg.setText('Value Error')
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
    def processNhan(self):
        try:
            a = float(self.sALineEdit.text())
            b = float(self.sBLineEdit.text())
            self.kTQuLineEdit.setText(str(b*a))
        except:
            dlg = QMessageBox()
            dlg.setWindowTitle('Warning')
            dlg.setText('Value Error')
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
    def processChia(self):
        try:
            a = float(self.sALineEdit.text())
            b = float(self.sBLineEdit.text())
            if b!=0:
                self.kTQuLineEdit.setText(str(b/a))
            else:
                dlg = QMessageBox()
                dlg.setWindowTitle('Warning')
                dlg.setText('Please enter coefficient b other than 0')
                dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
                dlg.setIcon(QMessageBox.Icon.Warning)
                dlg.exec()
        except:
            dlg = QMessageBox()
            dlg.setWindowTitle('Warning')
            dlg.setText('Value Error')
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()