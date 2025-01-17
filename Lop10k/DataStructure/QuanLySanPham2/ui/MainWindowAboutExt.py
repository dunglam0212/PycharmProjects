from PyQt6.QtCore import Qt

from DataStructure.QuanLySanPham2.ui.MainWindowAbout import Ui_MainWindow


class MainWindowAboutExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        #Dòng lệnh này có tác dụng đặt cửa sổ self.MainWindow ở chế độ độc quyền ứng dụng (application modal)
        #Người dùng không thể tương tác với các cửa sổ khác của ứng dụng.
        #Các cửa sổ khác của ứng dụng có thể bị vô hiệu hóa hoặc mờ đi.
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        pass