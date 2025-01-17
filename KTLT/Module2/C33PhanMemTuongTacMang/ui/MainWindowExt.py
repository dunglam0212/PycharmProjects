from PyQt6.QtWidgets import QMessageBox

from Module2.C33PhanMemTuongTacMang.Process import return_random_array, sum_array, find_smallest_item, increase_2_digit, \
    count_odds, sum_odds, sort_asc, sort_dsec
from Module2.C33PhanMemTuongTacMang.Tests import sum_odd, asc_arr
from Module2.C33PhanMemTuongTacMang.ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __int__(self):
        self.array_int = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonThoat.clicked.connect(self.processThoat)
        self.pushButtonXuatMangNgauNhien.clicked.connect(self.processXuatMangNgauNhien)
        self.pushButtonTinhTongMang.clicked.connect(self.processTinhTongMang)
        self.pushButtonTimPTNhoNhat.clicked.connect(self.processTimPTNhoNhat)
        self.pushButtonTangPT2.clicked.connect(self.processTangPT2)
        self.pushButtonDemPTLe.clicked.connect(self.processDemPTLe)
        self.pushButtonTongPTLe.clicked.connect(self.processTongPTLe)
        self.pushButtonSXMangTangDan.clicked.connect(self.processSXMangTangDan)
        self.pushButtonSXMangGiamDan.clicked.connect(self.processSXMangGiamDan)
    def processThoat(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Xác nhận thoát")
        msgBox.setText("Bạn có chắc chắn muốn thoát phần mềm không?")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes|
                                  QMessageBox.StandardButton.No)
        msgBox.setIcon(QMessageBox.Icon.Question)
        rs = msgBox.exec()
        if rs == QMessageBox.StandardButton.Yes:
            #self.MainWindow.close()
            exit()
    def processXuatMangNgauNhien(self):
        s= ''
        self.array_int = return_random_array()
        for item in self.array_int:
            s = s+str(item) + " "
        self.lineEditMangGoc.setText(s)
    def processTinhTongMang(self):
        rs = sum_array(self.array_int)
        self.lineEditKetQua.setText(str(rs))
    def processTimPTNhoNhat(self):
        rs = find_smallest_item(self.array_int)
        self.lineEditKetQua.setText(str(rs))
    def processTangPT2(self):
        s=''
        rs = increase_2_digit(self.array_int)
        for item in self.array_int:
            s = s + str(item) + " "
        self.lineEditKetQua.setText(s)
    def processDemPTLe(self):
        rs = count_odds(self.array_int)
        self.lineEditKetQua.setText(str(rs))
    def processTongPTLe(self):
        rs = sum_odds(self.array_int)
        self.lineEditKetQua.setText(str(rs))
    def processSXMangTangDan(self):
        s = ''
        rs = sort_asc(self.array_int)
        for item in self.array_int:
            s = s + str(item) + " "
        self.lineEditKetQua.setText(s)
    def processSXMangGiamDan(self):
        s = ''
        rs = sort_dsec(self.array_int)
        for item in self.array_int:
            s = s + str(item) + " "
        self.lineEditKetQua.setText(s)
