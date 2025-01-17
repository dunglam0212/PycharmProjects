from PyQt6.QtWidgets import QMessageBox

from DataStructure.QuanLySanPham2.tests.TestEmployeeDAL import employee_dal
from DataStructure.QuanLySanPham2.ui.MainWindowChangePassword import Ui_MainWindow


class MainWindowChangePasswordExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def print_login_infor(self):
        self.lineEditID.setText("Hoa")
        self.lineEditName.setText("1")
    def processSignalsAndSlot(self):
        #self.pushButtonChangePass.clicked.connect(self.processChangePass)
        pass
    def processChangePass(self):
        #B1: phải đăng nhập trc, nếu thành công thì cho đổi mật khẩu
        username = self.lineEditName.text()
        password = self.lineEditOldPass.text()
        '''employee_dal = EmployeeDAL()
        employee_dal.connect()
        emp = employee_dal.login(username, password)'''
        if username !="admin" and password != "123":
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText('Wrong Information! Please enter again')
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.exec()
        else:
            #b2: kiểm tra nhập lại mật khẩu mới có hợp lệ không
            new_pass = self.lineEditNewPass.text()
            confirm_new_pass = self.lineEditConfirmNewPass.text()
            if new_pass != confirm_new_pass:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Error")
                msgBox.setText('Confirm new password is not valid! Please enter again')
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.exec()
            else:
                #B3: đổi mật khẩu trên server
                id = int(self.lineEditID.text())
                result = employee_dal.changepassword(id, new_pass)
                if result>0:
                    msg = "Change Password Succeed"
                else:
                    msg = "Change Password Failed"
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Information")
                msgBox.setText(msg)
                msgBox.setIcon(QMessageBox.Icon.Information)
                msgBox.exec()