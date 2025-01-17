from PyQt6.QtWidgets import QMessageBox

from DoiNgoaiTeSangNoiTe.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonThoat.clicked.connect(self.processThoat)
        self.pushButtonTaoMoi.clicked.connect(self.processTaoMoi)
        self.pushButtonDoi.clicked.connect(self.processDoi)
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
    def processTaoMoi(self):
        self.lineEditSoLuongNgoaiTe.setText('')
        self.lineEditVND.setText('')
        self.comboBoxNgoaiTe.setCurrentIndex(0)
    def processDoi(self):
        try:
            cur_index = self.comboBoxNgoaiTe.currentIndex()
            ngoai_te = float(self.lineEditSoLuongNgoaiTe.text())
            if ngoai_te >0:
                if cur_index == 0:
                    vnd = ngoai_te*25.195
                    self.lineEditVND.setText(str(vnd))
                elif cur_index == 1:
                    vnd = ngoai_te*25.747
                    self.lineEditVND.setText(str(vnd))
                elif cur_index == 2:
                    vnd = ngoai_te*31.072
                    self.lineEditVND.setText(str(vnd))
                elif cur_index == 3:
                    vnd = ngoai_te*18.246
                    self.lineEditVND.setText(str(vnd))
                elif cur_index == 4:
                    vnd = ngoai_te*15.456
                    self.lineEditVND.setText(str(vnd))
                elif cur_index == 5:
                    vnd = ngoai_te*155.93
                    self.lineEditVND.setText(str(vnd))
                elif cur_index == 6:
                    vnd = ngoai_te*15.05
                    self.lineEditVND.setText(str(vnd))
                else:
                    vnd = ngoai_te*657.18
                    self.lineEditVND.setText(str(vnd))
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle('Cảnh báo lỗi')
                msgBox.setText('Dữ liệu bạn nhập không hợp lệ')
                msgBox.setInformativeText('Xin vui lòng nhập lại')
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                self.lineEditSoLuongNgoaiTe.setText('')
                self.lineEditSoLuongNgoaiTe.setFocus()
        except:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Cảnh báo lỗi')
            msgBox.setText('Dữ liệu bạn nhập không hợp lệ')
            msgBox.setInformativeText('Xin vui lòng nhập lại')
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            self.lineEditSoLuongNgoaiTe.setText('')
            self.lineEditSoLuongNgoaiTe.setFocus()

