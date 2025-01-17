from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QMessageBox

from Module7.C129TinhTienDien.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.lineEditChisocu.textChanged.connect(self.calculatekwh)
        self.lineEditChisomoi.textChanged.connect(self.calculatekwh)
        self.pushButtonKd.clicked.connect(self.processKd)
        self.pushButtonSx.clicked.connect(self.processSx)
        self.pushButtonSHBT.clicked.connect(self.processSHBT)
        self.pushButtonTinhtiep.clicked.connect(self.processTinhtiep)
        self.pushButtonHuongdan.clicked.connect(self.processHuongdan)
    def show(self):
        self.MainWindow.show()
    def calculatekwh(self):
        try:
            if self.lineEditChisocu.text() == '':
                a = 0
            else:
                a = self.lineEditChisocu.text()
            if self.lineEditChisomoi.text() == '':
                b = 0
            else:
                b = self.lineEditChisomoi.text()
            c = float(b)-float(a)
            self.lineEditkwh.setText(str(c))
        except:
            dlg = QMessageBox()
            dlg.setWindowTitle('Cảnh báo')
            dlg.setText('Vui lòng nhập các giá trị hợp lệ')
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
            self.lineEditChisocu.setText('')
            self.lineEditChisomoi.setText('')
            self.lineEditkwh.setText('')
            self.lineEditSoho.setText('')
    def processKd(self):
        try:
            a = float(self.lineEditChisocu.text())
            b = float(self.lineEditChisomoi.text())
            c = int(self.lineEditSoho.text())
            if a>0 and b>0 and c>0 and (b-a)>0:
                giakd = (b-a)*2320
                tien = giakd*c
                self.labelTienthu.setText(str(tien) + 'VND')
            else:
                dlg = QMessageBox()
                dlg.setWindowTitle('Cảnh báo')
                dlg.setText('Vui lòng nhập các giá trị hợp lệ')
                dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
                dlg.setIcon(QMessageBox.Icon.Warning)
                dlg.exec()
                self.lineEditChisocu.setText('')
                self.lineEditChisomoi.setText('')
                self.lineEditSoho.setText('')
        except:
            dlg = QMessageBox()
            dlg.setWindowTitle('Cảnh báo')
            dlg.setText('Vui lòng nhập các giá trị hợp lệ')
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
            self.lineEditChisocu.setText('')
            self.lineEditChisomoi.setText('')
            self.lineEditSoho.setText('')
    def processSx(self):
        try:
            a = float(self.lineEditChisocu.text())
            b = float(self.lineEditChisomoi.text())
            c = int(self.lineEditSoho.text())
            if a>0 and b>0 and c>0 and (b-a)>0:
                giasx = (b - a) * 1518
                tien = giasx * c
                self.labelTienthu.setText(str(tien) + 'VND')
            else:
                dlg = QMessageBox()
                dlg.setWindowTitle('Cảnh báo')
                dlg.setText('Vui lòng nhập các giá trị hợp lệ')
                dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
                dlg.setIcon(QMessageBox.Icon.Warning)
                dlg.exec()
                self.lineEditChisocu.setText('')
                self.lineEditChisomoi.setText('')
                self.lineEditSoho.setText('')
        except:
            dlg = QMessageBox()
            dlg.setWindowTitle('Cảnh báo')
            dlg.setText('Vui lòng nhập các giá trị hợp lệ')
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
            self.lineEditChisocu.setText('')
            self.lineEditChisomoi.setText('')
            self.lineEditSoho.setText('')
    def processSHBT(self):
        try:
            a = float(self.lineEditChisocu.text())
            b = float(self.lineEditChisomoi.text())
            c = int(self.lineEditSoho.text())
            if a>0 and b>0 and c>0 and (b-a)>0:
                if (b - a) <= (50 * c):
                    m = (b - a) * 1484
                    self.labelTienthu.setText(str(m) + 'VND')
                elif (b - a) <= (100 * c):
                    m = (50 * c * 1484) + ((b - a) - 50 * c) * 1533
                    self.labelTienthu.setText(str(m) + 'VND')
                elif (b - a) <= (200 * c):
                    m = (50 * c * 1484) + (50 * c * 1533) + ((b - a) - 100 * c) * 1786
                    self.labelTienthu.setText(str(m) + 'VND')
                elif (b - a) <= (300 * c):
                    m = (50 * c * 1484) + (50 * c * 1533) + (100 * c * 1786) + ((b - a) - 200 * c) * 2242
                    self.labelTienthu.setText(str(m) + 'VND')
                elif (b - a) <= (400 * c):
                    m = (50 * c * 1484) + (50 * c * 1533) + (100 * c * 1786) + (100 * c * 2242) + ((b - a) - 300 * c) * 2503
                    self.labelTienthu.setText(str(m) + 'VND')
                else:
                    m = (50 * c * 1484) + (50 * c * 1533) + (100 * c * 1786) + (100 * c * 2242) + (100 * c * 2503) + (
                                (b - a) - 400 * c) * 2587
                    self.labelTienthu.setText(str(m) + 'VND')
            else:
                dlg = QMessageBox()
                dlg.setWindowTitle('Cảnh báo')
                dlg.setText('Vui lòng nhập các giá trị hợp lệ')
                dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
                dlg.setIcon(QMessageBox.Icon.Warning)
                dlg.exec()
                self.lineEditChisocu.setText('')
                self.lineEditChisomoi.setText('')
                self.lineEditSoho.setText('')
        except:
            dlg = QMessageBox()
            dlg.setWindowTitle('Cảnh báo')
            dlg.setText('Vui lòng nhập các giá trị hợp lệ')
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
            self.lineEditChisocu.setText('')
            self.lineEditChisomoi.setText('')
            self.lineEditSoho.setText('')
    def processTinhtiep(self):
        self.lineEditChisocu.setText('')
        self.lineEditChisomoi.setText('')
        self.lineEditkwh.setText('')
        self.lineEditSoho.setText('')
        self.labelTienthu.setText('')
        QCursor.setPos(self.lineEditChisocu.mapToGlobal(self.lineEditChisocu.pos()))
    def processHuongdan(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Thông báo")
        dlg.setText("Đây là phần mềm tính tiền điện")
        dlg.setInformativeText("Kỹ sư thiết kế: Lâm Thùy Dung")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.exec()




