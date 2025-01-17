from cmath import sqrt

from PyQt6.QtWidgets import QMessageBox

from PhuongTrinhBac2.MainWindow import Ui_MainWindow

class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonThoat.clicked.connect(self.processThoat)
        self.pushButtonTiep.clicked.connect(self.processTiep)
        self.pushButtonGiai.clicked.connect(self.processGiai)
    def processThoat(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Xác nhận thoát')
        msgBox.setText('Bạn có chắc chắn muốn thoát không?')
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes|
                                  QMessageBox.StandardButton.No)
        rs = msgBox.exec()
        if rs == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
    def processTiep(self):
        self.lineEditHeSoA.setText('')
        self.lineEditHeSoB.setText('')
        self.lineEditHeSoC.setText('')
        self.labelKetQua.setText('')
        self.lineEditHeSoA.setFocus()
    def processGiai(self):
        try:
            a = float(self.lineEditHeSoA.text())
            b = float(self.lineEditHeSoB.text())
            c = float(self.lineEditHeSoC.text())
            delta = b * b - 4 * a * c
            if (a==0):
                if (b==0 and c==0):
                    self.labelKetQua.setText('Vô số nghiệm')
                elif (b==0 and c!=0):
                    self.labelKetQua.setText('Vô nghiệm')
                else:
                    kq = (-c/b)
                    self.labelKetQua.setText(f'Phương trình có nghiệm kép x1 = x2 = {kq}')
            elif (delta==0):
                kq = -b/(2*a)
                self.labelKetQua.setText(f'Phương trình có nghiệm kép x1 = x2 = {kq}')
            elif (delta>0):
                x1 = (-b-sqrt(delta))/(2*a)
                x2 = (-b + sqrt(delta)) / (2 * a)
                self.labelKetQua.setText(f'Phương trình có hai nghiệm phân biệt: x1 = {x1} và x2 = {x2}')
            else:
                self.labelKetQua.setText('Vô nghiệm')
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)  # Biểu tượng cảnh báo
            msg.setWindowTitle("Cảnh báo")
            msg.setText("Thông tin bạn nhập không hợp lệ!")
            msg.setInformativeText("Xin vui lòng nhập lại các hệ số đầu vào")
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()
            self.processTiep()



