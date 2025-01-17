from random import randrange

from PyQt6.QtWidgets import QMessageBox

from Module1.C24PhanMemLuckyNumber.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
        self.Tien_May = 100
        self.Tien_Nguoi = 100
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonKetThuc.clicked.connect(self.processKetThuc)
        self.pushButtonQuaySo.clicked.connect(self.processQuaySo)
        self.pushButtonGameMoi.clicked.connect(self.processGameMoi)
    def processKetThuc(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Xác nhận thoát')
        msgBox.setText('Bạn có chắc chắn muốn thoát không?')
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes|
                                  QMessageBox.StandardButton.No)
        rs = msgBox.exec()
        if rs == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
    def processQuaySo(self):
        if self.Tien_Nguoi>=30:
            self.Tien_May+=30
            self.Tien_Nguoi-=30
            so1 = randrange(9)
            so2 = randrange(10)
            so3 = randrange(11)
            self.labelSo1.setText(str(so1))
            self.labelSo2.setText(str(so2))
            self.labelSo3.setText(str(so3))
            if so1 == 7:
                Tien_Thuong = 100 + 0.5*self.Tien_May
                self.Tien_May*=0.5
                self.Tien_Nguoi+=Tien_Thuong
            if so2 == 7:
                Tien_Thuong = 30 + 0.5 * self.Tien_May
                self.Tien_May *= 0.5
                self.Tien_Nguoi += Tien_Thuong
            if so3 == 7:
                self.Tien_Nguoi+=10
            self.lineEditTienMay.setText(str(self.Tien_May))
            self.lineEditTienNguoi.setText(str(self.Tien_Nguoi))
    def processGameMoi(self):
        self.Tien_May = 100
        self.Tien_Nguoi = 100
        self.lineEditTienNguoi.setText(str(self.Tien_Nguoi))
        self.lineEditTienMay.setText(str(self.Tien_May))
        self.labelSo1.setText('7')
        self.labelSo2.setText('7')
        self.labelSo3.setText('7')



