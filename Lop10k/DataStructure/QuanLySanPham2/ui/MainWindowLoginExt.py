import traceback

from PyQt6.QtWidgets import QMessageBox, QMainWindow

from DataStructure.QuanLySanPham2.dal.EmployeeDAL import EmployeeDAL
from DataStructure.QuanLySanPham2.models.Employee import Employee
from DataStructure.QuanLySanPham2.ui.MainWindowExt import MainWindowExt
from DataStructure.QuanLySanPham2.ui.MainWindowLogin import Ui_MainWindow


class MainWindowLoginExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.processLogin)
    def processLogin(self):
        try:
            username = self.lineEditUserName.text()
            password = self.lineEditPassword.text()
            employee_dal = EmployeeDAL()
            employee_dal.connect()
            emp = employee_dal.login(username, password)
            if emp!=None:
                login_info = Employee(username=username, password=password, name="Hoa", id=1)
                #đóng màn hình đăng nhập
                self.MainWindow.close()
                #kích hoạt màn hình quản lý sản phẩm
                mainwindow=QMainWindow()
                self.mainUi= MainWindowExt()
                #self.mainUi=MainWindowProductExt()
                self.mainUi.login_emp=login_info
                self.mainUi.setupUi(mainwindow)
                self.mainUi.show_login_infor()
                # self.productUi.print_product_in_qtable()
                self.mainUi.show()
            else:
                msgBox = QMessageBox()
                msgBox.setText('Đăng nhập thất bại\nVui lòng kiểm tra lại thông tin đăng nhập')
                msgBox.setWindowTitle('Thông báo lỗi')
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.exec()
        except:
            traceback.print_exc()