# Form implementation generated from reading ui file 'C:\Users\Dung Lam\PycharmProjects\KTLT\FractionAdvanced\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(547, 751)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 171, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(162, 148, 249);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 491, 171))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background: rgb(245, 239, 255)")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditInput = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditInput.setGeometry(QtCore.QRect(140, 40, 301, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(10)
        self.lineEditInput.setFont(font)
        self.lineEditInput.setStyleSheet("background: rgb(205, 193, 255);\n"
"")
        self.lineEditInput.setObjectName("lineEditInput")
        self.lineEditQuantity = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditQuantity.setEnabled(False)
        self.lineEditQuantity.setGeometry(QtCore.QRect(140, 80, 301, 31))
        self.lineEditQuantity.setStyleSheet("background: rgb(205, 193, 255);")
        self.lineEditQuantity.setObjectName("lineEditQuantity")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditSortFrom = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditSortFrom.setGeometry(QtCore.QRect(140, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(10)
        self.lineEditSortFrom.setFont(font)
        self.lineEditSortFrom.setStyleSheet("background: rgb(205, 193, 255);\n"
"")
        self.lineEditSortFrom.setObjectName("lineEditSortFrom")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(270, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEditSortTo = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditSortTo.setGeometry(QtCore.QRect(330, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(10)
        self.lineEditSortTo.setFont(font)
        self.lineEditSortTo.setStyleSheet("background: rgb(205, 193, 255);\n"
"")
        self.lineEditSortTo.setObjectName("lineEditSortTo")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 250, 491, 111))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background: rgb(245, 239, 255)")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButtonNew = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonNew.setGeometry(QtCore.QRect(10, 40, 61, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonNew.setFont(font)
        self.pushButtonNew.setStyleSheet("background: rgb(205, 193, 255);")
        self.pushButtonNew.setObjectName("pushButtonNew")
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonSave.setGeometry(QtCore.QRect(250, 40, 61, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setStyleSheet("background: rgb(205, 193, 255);")
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonRemove = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonRemove.setGeometry(QtCore.QRect(330, 40, 61, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRemove.setFont(font)
        self.pushButtonRemove.setStyleSheet("background: rgb(205, 193, 255);")
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonExit.setGeometry(QtCore.QRect(410, 40, 61, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonExit.setFont(font)
        self.pushButtonExit.setStyleSheet("background: rgb(205, 193, 255);")
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.pushButtonSort = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonSort.setGeometry(QtCore.QRect(90, 40, 61, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSort.setFont(font)
        self.pushButtonSort.setStyleSheet("background: rgb(205, 193, 255);")
        self.pushButtonSort.setObjectName("pushButtonSort")
        self.pushButtonFind = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonFind.setGeometry(QtCore.QRect(170, 40, 61, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonFind.setFont(font)
        self.pushButtonFind.setStyleSheet("background: rgb(205, 193, 255);")
        self.pushButtonFind.setObjectName("pushButtonFind")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 380, 241, 311))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background: rgb(245, 239, 255)")
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget = QtWidgets.QListWidget(parent=self.groupBox_3)
        self.listWidget.setGeometry(QtCore.QRect(20, 30, 201, 261))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(11)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background: rgb(205, 193, 255);")
        self.listWidget.setObjectName("listWidget")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(280, 380, 231, 311))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("background: rgb(245, 239, 255)")
        self.groupBox_4.setObjectName("groupBox_4")
        self.listWidgetSort = QtWidgets.QListWidget(parent=self.groupBox_4)
        self.listWidgetSort.setGeometry(QtCore.QRect(20, 30, 191, 261))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Arima Madurai ExtraBo")
        font.setPointSize(11)
        self.listWidgetSort.setFont(font)
        self.listWidgetSort.setStyleSheet("background: rgb(205, 193, 255);")
        self.listWidgetSort.setObjectName("listWidgetSort")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "FRACTION"))
        self.groupBox.setTitle(_translate("MainWindow", "Input:"))
        self.label_2.setText(_translate("MainWindow", "Input fraction:"))
        self.label_3.setText(_translate("MainWindow", "Quantity:"))
        self.label_4.setText(_translate("MainWindow", "Sort from:"))
        self.label_5.setText(_translate("MainWindow", "Sort to:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Functions:"))
        self.pushButtonNew.setText(_translate("MainWindow", "New"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonRemove.setText(_translate("MainWindow", "Remove"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))
        self.pushButtonSort.setText(_translate("MainWindow", "Sort"))
        self.pushButtonFind.setText(_translate("MainWindow", "Find"))
        self.groupBox_3.setTitle(_translate("MainWindow", "List Fraction:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "List Sort Fraction:"))
