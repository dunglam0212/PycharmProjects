import traceback

from PyQt6.QtWidgets import QMainWindow

from DataStructure.QuanLySanPham2.ui.MainWindow import Ui_MainWindow
from DataStructure.QuanLySanPham2.ui.MainWindowChangePasswordExt import MainWindowChangePasswordExt


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.statusbar.addWidget(self.labelWelcome)
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def show_login_infor(self):
        login_html_welcome = f"<font color='red'>Xin chào:</font> {self.login_emp.name}"
        self.labelWelcome.setText(login_html_welcome)

    def processSignalsAndSlot(self):
        self.actionChangePass.triggered.connect(self.processOpenMainWindowChangePassword)
    def processOpenMainWindowChangePassword(self):
        try:
            self.mainwindowchangepass = QMainWindow()
            self.changepassUi = MainWindowChangePasswordExt()
            self.changepassUi.setupUi(self.mainwindowchangepass)
            self.changepassUi.print_login_infor()
            self.changepassUi.show()
        except:
            traceback.print_exc()
