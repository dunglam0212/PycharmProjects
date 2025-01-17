import traceback

import mysql.connector
from PyQt6.QtWidgets import QTableWidgetItem

from LearnPyQtDesign.S48PythonMySQLconnector.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.id = None
        self.code = None
        self.name = None
        self.age = None
        self.avatar = None
        self.intro = None
        self.host = "localhost"
        self.user = "root"
        self.port = 3306
        self.password = "dungcute0212"
        self.database = "employeemanagement"

        # Kết nối với cơ sở dữ liệu
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database)
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
    def show(self):
        self.MainWindow.show()
    def connectMySQL(self):
        try:
            server = "localhost"
            port = 3306
            database = "employeemanagement"
            username = "root"
            password = "dungcute0212"

            self.conn = mysql.connector.connect(
                host=server,
                port=port,
                database = database,
                user=username,
                password=password
            )
        except:
            traceback.print_exc()
    def selectAllStudent(self):
        try:
            cursor = self.conn.cursor()
            sql = "SELECT * FROM student"
            cursor.execute(sql)
            dataset = cursor.fetchall()
            print(dataset)
            self.tableWidget.setRowCount(0)
            row=0
            for item in dataset:
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)

                self.id = item[0]
                self.code=item[1]
                self.name=item[2]
                self.age=item[3]
                self.avatar=item[4]
                self.intro=item[5]

                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(self.id)))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(self.code))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(self.name))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(self.age)))

            cursor.close()
        except:
            traceback.print_exc()
