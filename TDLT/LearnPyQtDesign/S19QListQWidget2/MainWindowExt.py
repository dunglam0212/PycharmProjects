import json
import os.path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox, QListWidget

from LearnPyQtDesign.S19QListQWidget2.Employee import Employee
from LearnPyQtDesign.S19QListQWidget2.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.dataset = []
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.readEmployeeFromJson()
        self.pushButtonNew.clicked.connect(self.processNew)
        self.pushButtonSave.clicked.connect(self.processSave)
        self.pushButtonDelete.clicked.connect(self.processDelete)
        self.pushButtonClose.clicked.connect(self.processClose)
        self.listWidget.itemSelectionChanged.connect(self.processitemSelectionChanged)
    def show(self):
        self.MainWindow.show()
    def processNew(self):
        self.lineEditName.setText('')
        self.lineEditEmail.setText('')
        self.lineEditName.setFocus()
    def writeEmployeeToJson(self):
        dataset = []
        for i in range(0, self.listWidget.count()):
            item = self.listWidget.item(i)
            emp = item.data(Qt.ItemDataRole.UserRole)
            dataset.append(emp)
        jsonString = json.dumps([emp.__dict__ for emp in dataset])
        jsonFile = open("database.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    def readEmployeeFromJson(self):
        if os.path.isfile("database.json") == False:
            return
        file = open('database.json', "r")
        # Reading from file
        self.dataset = json.loads(file.read(), object_hook=lambda d: Employee(**d))
        file.close()
        for emp in self.dataset:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, emp)
            item.setText(str(emp))
            item.setCheckState(Qt.CheckState.Unchecked)
            if emp.gender == True:
                item.setIcon(QIcon("images/ic_woman.png"))
            else:
                item.setIcon(QIcon("images/ic_man.png"))
            self.listWidget.addItem(item)
    def processSave(self):
        insertEmployee = Employee(self.lineEditName.text(), self.lineEditEmail.text(),self.radioButtonWoman.isChecked())
        isDuplicated = False #Biến để xét xem dữ liệu ng dùng muốn lưu có trùng với dữ liệu hiện có hay kh
        for i in range(0, self.listWidget.count()):
            item = self.listWidget.item(i)
            data = item.data(Qt.ItemDataRole.UserRole)
            if insertEmployee.email.lower()==data.email.lower():
                isDuplicated=True
                break
        if not isDuplicated:
            item=QListWidgetItem() #Nếu kh trùng thì tạo item mới cho danh sách
        item.setData(Qt.ItemDataRole.UserRole, insertEmployee)
        item.setText(str(insertEmployee))
        item.setCheckState(Qt.CheckState.Unchecked)
        if self.radioButtonWoman.isChecked():
            item.setIcon(QIcon('images/ic_woman.png'))
        else:
            item.setIcon(QIcon('images/ic_man.png'))
        if not isDuplicated:
            self.listWidget.addItem((item)) #Nếu kh trùng thì thêm mới item đó vào danh sách
        self.writeEmployeeToJson()
    def processDelete(self):
        answer = QMessageBox.question(
            self.MainWindow,
            'Confirmation',
            'Do you want to remove checked Items?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No)
        if answer == QMessageBox.StandardButton.No:
            return
        for index in range(self.listWidget.count() - 1, -1, -1):
            item = self.listWidget.item(index)
            if item.checkState() == Qt.CheckState.Checked:
                emp = item.data(Qt.ItemDataRole.UserRole)
                self.dataset.remove(emp)
                current_item = self.listWidget.takeItem(index)
                del current_item
        self.processNew()
        self.writeEmployeeToJson()
        self.readEmployeeFromJson()
    def processClose(self):
        answer = QMessageBox.question(self.MainWindow,
                                      'Confirmation',
                                      'Do you want to exit?',
                                      QMessageBox.StandardButton.Yes|
                                      QMessageBox.StandardButton.No)
        if answer == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
    def processitemSelectionChanged(self):
        current_row = self.listWidget.currentRow()
        if current_row >=0:
            item = self.listWidget.item(current_row)
            emp = item.data(Qt.ItemDataRole.UserRole)
            self.lineEditName.setText(emp.name)
            self.lineEditEmail.setText(emp.email)
            if emp.gender==True:
                self.radioButtonWoman.setChecked(True)
            else:
                self.radioButtonMan.setChecked(True)

