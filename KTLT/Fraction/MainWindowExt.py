from PyQt6.QtWidgets import QMessageBox

from Fraction.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        #super() là gọi setupUi của cha nó
        self.MainWindow = MainWindow
        #Lưu biến local/tham số hình thức MainWindow
        #Nếu kh lưu trữ thì nó sẽ bị mất
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
        #hiển thị giao diện để người dùng tương tác
    def processSignalsAndSlot(self):
        self.pushButtonThoat.clicked.connect(self.processThoat)
        self.pushButtonTiep.clicked.connect(self.processTiep)
        self.pushButtonCong.clicked.connect(self.processCong)
        self.pushButtonTru.clicked.connect(self.processTru)
        self.pushButtonNhan.clicked.connect(self.processNhan)
        self.pushButtonChia.clicked.connect(self.processChia)
    def processThoat(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Xác nhận thoát')
        msgBox.setText('Bạn có chắc chắn muốn thoát không?')
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes |
                                  QMessageBox.StandardButton.No)
        rs = msgBox.exec()
        if rs == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()

    def processTiep(self):
        self.lineEditTuSo1.setText('')
        self.lineEditMauSo1.setText('')
        self.lineEditTuSo2.setText('')
        self.lineEditMauSo2.setText('')
        self.labelKetQua.setText('')
    def WarningMessageBox(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Cảnh báo lỗi!')
        msgBox.setText('Giá trị bạn nhập không hợp lệ!')
        msgBox.setInformativeText('Xin vui lòng nhập lại sau!')
        msgBox.setIcon(QMessageBox.Icon.Warning)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
        msgBox.exec()
    def processCong(self):
        try:
            TuSo1 = int(self.lineEditTuSo1.text())
            MauSo1 = int(self.lineEditMauSo1.text())
            TuSo2 = int(self.lineEditTuSo2.text())
            MauSo2 = int(self.lineEditMauSo2.text())
            if MauSo1 != 0 and MauSo2!=0:
                kq = (TuSo1*MauSo2 + TuSo2*MauSo1)/(MauSo1*MauSo2)
                self.labelKetQua.setText(f'{TuSo1}/{MauSo1} + {TuSo2}/{MauSo2} = {kq}')
            elif MauSo1==0 or MauSo2==0:
                msgBox = QMessageBox()
                msgBox.setWindowTitle('Cảnh báo lỗi!')
                msgBox.setText('Mẫu số không được bằng 0!')
                msgBox.setInformativeText('Xin vui lòng nhập lại mẫu số!')
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
                msgBox.exec()
            else:
                self.WarningMessageBox()
        except:
            self.WarningMessageBox()
    def processTru(self):
        try:
            TuSo1 = int(self.lineEditTuSo1.text())
            MauSo1 = int(self.lineEditMauSo1.text())
            TuSo2 = int(self.lineEditTuSo2.text())
            MauSo2 = int(self.lineEditMauSo2.text())
            if MauSo1 != 0 and MauSo2!=0:
                kq = (TuSo1*MauSo2 - TuSo2*MauSo1)/(MauSo1*MauSo2)
                self.labelKetQua.setText(f'{TuSo1}/{MauSo1} - {TuSo2}/{MauSo2} = {kq}')
            elif MauSo1==0 or MauSo2==0:
                msgBox = QMessageBox()
                msgBox.setWindowTitle('Cảnh báo lỗi!')
                msgBox.setText('Mẫu số không được bằng 0!')
                msgBox.setInformativeText('Xin vui lòng nhập lại mẫu số!')
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
                msgBox.exec()
            else:
                self.WarningMessageBox()
        except:
            self.WarningMessageBox()
    def processNhan(self):
        try:
            TuSo1 = int(self.lineEditTuSo1.text())
            MauSo1 = int(self.lineEditMauSo1.text())
            TuSo2 = int(self.lineEditTuSo2.text())
            MauSo2 = int(self.lineEditMauSo2.text())
            if MauSo1 != 0 and MauSo2!=0:
                kq = (TuSo1*TuSo2)/(MauSo1*MauSo2)
                self.labelKetQua.setText(f'{TuSo1}/{MauSo1} * {TuSo2}/{MauSo2} = {kq}')
            elif MauSo1==0 or MauSo2==0:
                msgBox = QMessageBox()
                msgBox.setWindowTitle('Cảnh báo lỗi!')
                msgBox.setText('Mẫu số không được bằng 0!')
                msgBox.setInformativeText('Xin vui lòng nhập lại mẫu số!')
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
                msgBox.exec()
            else:
                self.WarningMessageBox()
        except:
            self.WarningMessageBox()
    def processChia(self):
        try:
            TuSo1 = int(self.lineEditTuSo1.text())
            MauSo1 = int(self.lineEditMauSo1.text())
            TuSo2 = int(self.lineEditTuSo2.text())
            MauSo2 = int(self.lineEditMauSo2.text())
            if MauSo1 != 0 and MauSo2!=0 and TuSo2!=0:
                kq = (TuSo1*MauSo2)/(MauSo1*TuSo2)
                self.labelKetQua.setText(f'{TuSo1}/{MauSo1} / {TuSo2}/{MauSo2} = {kq}')
            elif MauSo1==0 or MauSo2==0:
                msgBox = QMessageBox()
                msgBox.setWindowTitle('Cảnh báo lỗi!')
                msgBox.setText('Mẫu số không được bằng 0!')
                msgBox.setInformativeText('Xin vui lòng nhập lại mẫu số!')
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
                msgBox.exec()
            elif TuSo2==0:
                msgBox = QMessageBox()
                msgBox.setWindowTitle('Cảnh báo lỗi!')
                msgBox.setText('Tử số của phân số 2 không được bằng 0!')
                msgBox.setInformativeText('Xin vui lòng nhập lại!')
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                self.lineEditTuSo2.setText('')
                self.lineEditTuSo2.setFocus()
            else:
                self.WarningMessageBox()
        except:
            self.WarningMessageBox()
