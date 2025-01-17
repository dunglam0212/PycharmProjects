from PyQt6.QtWidgets import QMessageBox

from Module1.C22PhanMemTinhBongDenHu.MainWindow import Ui_MainWindow
from Module1.C22PhanMemTinhBongDenHu.TinhXacSuatBongDenHu import xac_suat_den_hu


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonLamMoi.clicked.connect(self.processLamMoi)
        self.pushButtonThoat.clicked.connect(self.processThoat)
        self.pushButtonTinh.clicked.connect(self.processTinh)
    def processLamMoi(self):
        self.lineEditD.setText('')
        self.lineEditM.setText('')
        self.lineEditN.setText('')
        self.labelKetQua.setText('')
        self.lineEditN.setFocus()
    def processThoat(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Xác nhận thoát')
        msgBox.setText('Bạn có chắc chắn muốn thoát chương trình không?')
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes|
                                  QMessageBox.StandardButton.No)
        rs = msgBox.exec()
        if rs == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
        else:
            self.processLamMoi()
    def processTinh(self):
        try:
            N = int(self.lineEditN.text())
            D = int(self.lineEditD.text())
            M = int(self.lineEditM.text())
            if N>=D and N>=M and N>0:
                p = xac_suat_den_hu(N,D,M)
                self.labelKetQua.setText(f'{p}')
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle('Cảnh báo')
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setText('Thông tin bạn nhập không hợp lệ!')
                msgBox.setInformativeText('Xin vui lòng nhập lại!')
                msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                self.processLamMoi()
        except:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Cảnh báo')
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText('Thông tin bạn nhập không hợp lệ!')
            msgBox.setInformativeText('Xin vui lòng nhập lại!')
            msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            self.processLamMoi()
