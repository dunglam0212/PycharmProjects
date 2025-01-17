from PyQt6.QtWidgets import QCompleter, QLineEdit

from LearnPyQtDesign.S12LearnQLineEditBasicWidgets.MainWIndow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        cities = ['Hà Nội', 'Đà Nẵng', 'Huế', 'Đà Lạt', 'Cần Thơ', 'Sóc Trăng', 'Hồ Chí Minh']
        completer = QCompleter(cities)
        self.cityProvinceLineEdit.setCompleter(completer)
    def show(self):
        self.MainWindow.show()
