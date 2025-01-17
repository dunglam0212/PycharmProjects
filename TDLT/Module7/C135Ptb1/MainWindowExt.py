from PyQt6.QtWidgets import QMessageBox

from Module7.C135Ptb1.MainWindow import Ui_MainWindow

class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonGiai.clicked.connect(self.processGiai)
        self.pushButtonTiep.clicked.connect(self.processTiep)
        self.pushButtonThoat.clicked.connect(self.processThoat)
    def show(self):
        self.MainWindow.show()
    def processGiai(self):
        try:
            a = float(self.hSALineEdit.text())
            b = float(self.hSBLineEdit.text())
            if a==0 and b==0:
                self.lineEditKqua.setText('Phương trình vô số nghiệm')
            elif a==0 and b!=0:
                self.lineEditKqua.setText('Phương trình vô nghiệm')
            else:
                self.lineEditKqua.setText(str(round(-b/a,5)))
        except:
            dlg = QMessageBox()
            dlg.setWindowTitle('Cảnh báo')
            dlg.setText('Vui lòng nhập các hệ số a, b là các số thực')
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
            self.hSALineEdit.setText('')
            self.hSBLineEdit.setText('')
    def processTiep(self):
        self.hSALineEdit.setText('')
        self.hSBLineEdit.setText('')
        self.lineEditKqua.setText('')
    def processThoat(self):
        dlg = QMessageBox()
        dlg.setWindowTitle('Thoát')
        dlg.setText('Bạn có muốn thoát không?')
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes|
                               QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
        else:
            pass

