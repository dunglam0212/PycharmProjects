from Module7.C128ChuyenDuongLichThanhAmLich.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonChuyen.clicked.connect(self.processChuyen)
    def show(self):
        self.MainWindow.show()
    def processChuyen(self):

