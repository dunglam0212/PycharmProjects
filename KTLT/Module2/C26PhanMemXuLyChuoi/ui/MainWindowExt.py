from PyQt6.QtWidgets import QMessageBox

from Module2.C26PhanMemXuLyChuoi.model.XuLyChuoi import count_capital_character, list_uppercase, print_uppercase, \
    print_lowercase, count_lowercase, count_vowels, count_consonants, count_a_word
from Module2.C26PhanMemXuLyChuoi.ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonKetThuc.clicked.connect(self.processKetThuc)
        self.pushButtonNhap.clicked.connect(self.processNhap)
        self.pushButtonDemKTHoa.clicked.connect(self.processDemKTHoa)
        self.pushButtonInChuHoa.clicked.connect(self.processInChuHoa)
        self.pushButtonInChuThuong.clicked.connect(self.processInChuThuong)
        self.pushButtonDemSoKTThuong.clicked.connect(self.processDemKTThuong)
        self.pushButtonInNguyenAmPhuAm.clicked.connect(self.procesInNguyenAmPhuAm)
        self.pushButtonDemSoTu.clicked.connect(self.processDemSoTu)
    def processKetThuc(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Xác nhận thoát")
        msgBox.setText("Bạn có chắc chắn muốn thoát không?")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes|
                                  QMessageBox.StandardButton.No)
        msgBox.setIcon(QMessageBox.Icon.Question)
        rs = msgBox.exec()
        if rs == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
    def processNhap(self):
        if self.textEditNhap.toPlainText() == "":
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Cảnh báo lỗi")
            msgBox.setText("Vui lòng nhập một chuỗi bất kỳ vào ô nhập liệu!")
            msgBox.setInformativeText("Chuỗi không thể chỉ có mỗi dấu cách (khoảng trắng)!")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.exec()
        else:
            self.pushButtonDemKTHoa.setEnabled(True)
            self.pushButtonInChuHoa.setEnabled(True)
            self.pushButtonDemSoTu.setEnabled(True)
            self.pushButtonInChuThuong.setEnabled(True)
            self.pushButtonInNguyenAmPhuAm.setEnabled(True)
            self.pushButtonDemSoKTThuong.setEnabled(True)
            self.pushButtonInSoTuTrenMoiDong.setEnabled(True)
    def processDemKTHoa(self):
        string = self.textEditNhap.toPlainText()
        rs = count_capital_character(string)
        self.textEditKetQua.setPlainText(f"Số ký tự in hoa trong chuỗi '{string}' là: {rs}")
    def processInChuHoa(self):
        string = self.textEditNhap.toPlainText()
        ListUppercase = print_uppercase(string)
        self.textEditKetQua.setPlainText(f"Các ký tự in hoa trong chuỗi '{string}' là: {ListUppercase}")
    def processInChuThuong(self):
        string = self.textEditNhap.toPlainText()
        ListLowercase = print_lowercase(string)
        self.textEditKetQua.setPlainText(f"Các ký tự in hoa trong chuỗi '{string}' là: {ListLowercase}")
    def processDemKTThuong(self):
        string = self.textEditNhap.toPlainText()
        rs = count_lowercase(string)
        self.textEditKetQua.setPlainText(f"Số ký tự thường trong chuỗi '{string}' là: {rs}")
    def procesInNguyenAmPhuAm(self):
        string = self.textEditNhap.toPlainText()
        List_Vowels = count_vowels(string)
        List_Consonants = count_consonants(string)
        self.textEditKetQua.setPlainText(f"- Số nguyên âm trong chuỗi '{string}' là: {List_Vowels}\n- Số phụ âm trong chuỗi '{string}' là: {List_Consonants}")
    def processDemSoTu(self):
        string = self.textEditNhap.toPlainText()
        list = count_a_word(string)
        self.textEditKetQua.setPlainText(f"Số từ trong chuỗi '{string}' là: {list}")


