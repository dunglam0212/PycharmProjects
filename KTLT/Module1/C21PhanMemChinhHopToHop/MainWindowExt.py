from PyQt6.QtWidgets import QMessageBox

from Module1.C21PhanMemChinhHopToHop.MainWindow import Ui_MainWindow
from Module1.C21PhanMemChinhHopToHop.TinhChinhHopToHop import chinh_hop, to_hop


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.processThuchien)
    def show(self):
        self.MainWindow.show()
    def processTiep(self):
        self.lineEditNhapN.setText('')
        self.lineEditNhapK.setText('')
        self.lineEditA.setText('')
        self.lineEditC.setText('')
        self.lineEditNhapN.setFocus()
    def processThuchien(self):
        try:
            k = int(self.lineEditNhapK.text())
            n = int(self.lineEditNhapN.text())
            if n>k and k>=0:
                ch = chinh_hop(k,n)
                th = to_hop(k,n)
                self.lineEditA.setText(f'{ch}')
                self.lineEditC.setText(f'{th}')
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setWindowTitle('Cảnh báo')
                msgBox.setText('K hoặc N mà bạn nhập không hợp lệ!')
                msgBox.setInformativeText('Vui lòng nhập lại!')
                msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                self.processTiep()
        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setWindowTitle('Cảnh báo')
            msgBox.setText('K hoặc N mà bạn nhập không hợp lệ!')
            msgBox.setInformativeText('Vui lòng nhập lại!')
            msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            self.processTiep()

