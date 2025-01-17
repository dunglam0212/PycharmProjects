from PyQt6.QtWidgets import QMessageBox

from Module1.C23PhanMemBanSach.ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.Tong_KH = 0
        self.Tong_SV = 0
        self.Tong_Doanh_thu = 0
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonThoat.clicked.connect(self.processThoat)
        self.pushButtonBanMoi.clicked.connect(self.processBanMoi)
        self.pushButtonTinh.clicked.connect(self.processTinh)
        self.pushButtonThongKe.clicked.connect(self.processThongKe)
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
    def processBanMoi(self):
        self.lineEditTenKH.setText('')
        self.lineEditSoLuong.setText('')
        self.lineEditThanhTien.setText('')
        self.checkBoxSV.setChecked(False)
        self.lineEditTenKH.setFocus()
    def processNhapThongTin(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Thông tin')
        msgBox.setText('Tên Khách hàng không được để trống')
        msgBox.setInformativeText('Số lượng sách phải là một số nguyên dương' + ' '
                                  +'Mỗi quyển sách được bán với giá là 20000')
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
        msgBox.exec()
    def processTinhSoLuong(self):
        try:
            So_Luong = int(self.lineEditSoLuong.text())
            if So_Luong>0:
                return So_Luong
            else:
                return False
        except:
            return False
    def processTinh(self):
        if self.lineEditTenKH.text() == '':
            self.processNhapThongTin()
            self.lineEditTenKH.setFocus()
        else:
            So_Luong = self.processTinhSoLuong()
            if So_Luong == False:
                self.processNhapThongTin()
                self.lineEditSoLuong.setText('')
                self.lineEditSoLuong.setFocus()
            else:
                if self.checkBoxSV.isChecked() == True:
                    Thanh_Tien = So_Luong * 20000 * 0.95
                    self.lineEditThanhTien.setText(f'{Thanh_Tien}')
                    self.Tong_SV+=1
                    self.Tong_KH+=1
                    self.Tong_Doanh_thu = self.Tong_Doanh_thu + Thanh_Tien
                else:
                    Thanh_Tien = So_Luong * 20000
                    self.lineEditThanhTien.setText(f'{Thanh_Tien}')
                    self.Tong_KH += 1
                    self.Tong_Doanh_thu = self.Tong_Doanh_thu + Thanh_Tien
        '''
        Cách 2: Không cần lưu biến Tong_Doanh_Thu
        self.so_luong_mua_kh=0
        self.so_luong_mua_khsv=0
        name=self.lineEditTenKh.text()
        quantity = self.lineEditSoLuong.text()
        if self.checkboxSV.isChecked()==True:
            self.so_luong_khsv +=1
            self.so_luong_mua_khsv += quantity
            money = quantity*20000*0.95
            self.lineEditThanhTien.setTextf'{money}')
        else:
            self.so_luong_kh +=1
            self.so_luong_mua_kh += quantity
            money = quantity*20000
            self.lineEditThanhTien.setTextf'{money}')
            '''
    def processThongKe(self):
        self.lineEditTongSoKH.setText(str(self.Tong_KH))
        self.lineEditTongSV.setText(str(self.Tong_SV))
        self.lineEditTongDoanhThu.setText(str(self.Tong_Doanh_thu))