# Form implementation generated from reading ui file 'C:\Users\Dung Lam\PycharmProjects\KTLT\Module1\C21PhanMemChinhHopToHop\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 603)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background: rgb(215, 239, 255);\n"
"color: rgb(255, 0, 127);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.groupBoxNhap = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxNhap.setGeometry(QtCore.QRect(40, 90, 361, 101))
        self.groupBoxNhap.setStyleSheet("background: rgb(229, 255, 217);")
        self.groupBoxNhap.setObjectName("groupBoxNhap")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBoxNhap)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 61, 21))
        self.label_2.setObjectName("label_2")
        self.lineEditNhapN = QtWidgets.QLineEdit(parent=self.groupBoxNhap)
        self.lineEditNhapN.setGeometry(QtCore.QRect(80, 30, 251, 20))
        self.lineEditNhapN.setStyleSheet("background: rgb(255, 226, 249)")
        self.lineEditNhapN.setObjectName("lineEditNhapN")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBoxNhap)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 61, 21))
        self.label_3.setObjectName("label_3")
        self.lineEditNhapK = QtWidgets.QLineEdit(parent=self.groupBoxNhap)
        self.lineEditNhapK.setGeometry(QtCore.QRect(80, 60, 251, 20))
        self.lineEditNhapK.setStyleSheet("background: rgb(255, 226, 249)")
        self.lineEditNhapK.setObjectName("lineEditNhapK")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 210, 111, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Dung Lam\\PycharmProjects\\KTLT\\Module1\\C21PhanMemChinhHopToHop\\images/ic_calculate.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.groupBoxKetQua = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxKetQua.setGeometry(QtCore.QRect(40, 280, 361, 101))
        self.groupBoxKetQua.setStyleSheet("background: rgb(225, 231, 255);")
        self.groupBoxKetQua.setObjectName("groupBoxKetQua")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBoxKetQua)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 61, 21))
        self.label_4.setObjectName("label_4")
        self.lineEditA = QtWidgets.QLineEdit(parent=self.groupBoxKetQua)
        self.lineEditA.setEnabled(False)
        self.lineEditA.setGeometry(QtCore.QRect(80, 30, 251, 20))
        self.lineEditA.setStyleSheet("background: rgb(225, 241, 255)")
        self.lineEditA.setObjectName("lineEditA")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBoxKetQua)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 61, 21))
        self.label_5.setObjectName("label_5")
        self.lineEditC = QtWidgets.QLineEdit(parent=self.groupBoxKetQua)
        self.lineEditC.setEnabled(False)
        self.lineEditC.setGeometry(QtCore.QRect(80, 60, 251, 20))
        self.lineEditC.setStyleSheet("background: rgb(225, 241, 255)")
        self.lineEditC.setObjectName("lineEditC")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditNhapN, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.lineEditA)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff007f;\">Chỉnh hợp và tổ hợp</span></p></body></html>"))
        self.groupBoxNhap.setTitle(_translate("MainWindow", "Nhập N và K: "))
        self.label_2.setText(_translate("MainWindow", "Nhập N: "))
        self.label_3.setText(_translate("MainWindow", "Nhập K: "))
        self.pushButton.setText(_translate("MainWindow", "Thực hiện"))
        self.groupBoxKetQua.setTitle(_translate("MainWindow", "Kết quả:"))
        self.label_4.setText(_translate("MainWindow", "A ="))
        self.label_5.setText(_translate("MainWindow", "C = "))
