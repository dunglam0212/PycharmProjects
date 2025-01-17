import base64
import traceback

import mysql.connector
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidgetItem, QFileDialog

from LearnPyQtDesign.S49MySQLPart1.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.default_avatar = "images/ic_picture.png"
        self.id = None
        self.code = None
        self.name = None
        self.age = None
        self.avatar = None
        self.intro = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.tableWidgetListStudent.itemSelectionChanged.connect(self.processitemSelectionChanged)
        self.pushButtonAvatar.clicked.connect(self.processbtnAvatar)
        self.pushButtonRemoveAvatar.clicked.connect(self.processbtnRemoveAvatar)
        #self.pushButtonNew.clicked.connect(self.processbtnNew)
        #self.pushButtonInsert.clicked.connect(self.processbtnInsert)
        #self.pushButtonUpdate.clicked.connect(self.processbtnUpdate)
        #self.pushButtonRemove.clicked.connect(self.processbtnRemove)
    def show(self):
        self.MainWindow.show()
    def connectMySQL(self):
        try:
            #Kết nối với MySQL Server
            server = 'localhost'
            port = 3306
            database = 'studentmanagement_test'
            username = 'root'
            password = 'dungcute0212'

            self.conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password
            )
        except:
            traceback.print_exc()
    def selectAllStudent(self):
        try:
            # Hàm truy vấn toàn bộ Student và hiển thị lên QListWidget
            cursor = self.conn.cursor()
            # query all students
            sql = "select * from student"
            cursor.execute(sql)
            dataset = cursor.fetchall()
            self.tableWidgetListStudent.setRowCount(0)
            row = 0
            for item in dataset:
                row = self.tableWidgetListStudent.rowCount()
                self.tableWidgetListStudent.insertRow(row)

                self.id = item[0]
                self.code = item[1]
                self.name = item[2]
                self.age = item[3]
                self.avatar = [4]
                self.intro = item[5]

                self.tableWidgetListStudent.setItem(row, 0, QWidgetItem(str(self.id)))
                self.tableWidgetListStudent.setItem((row, 1, QWidgetItem(self.code)))
                self.tableWidgetListStudent.setItem(row, 2, QWidgetItem(self.name))
                self.tableWidgetListStudent.setItem((row, 3, QWidgetItem(str(self.age))))

            cursor.close()
        except:
            traceback.print_exc()
    def processitemSelectionChanged(self):
        row = self.tableWidgetListStudent.currentRow()
        if row==-1:
            return
        try:
            code = self.tableWidgetListStudent.item(row,1).text()
            cursor=self.conn.cursor()
            #query all students
            sql = "SELECT * FROM student where code=%s"
            val = (code,)
            cursor.execute(sql, val)
            item = cursor.fetchone()
            if item !=None:
                self.id=item[0]
                self.code=item[1]
                self.name=item[2]
                self.age=item[3]
                self.avatar=item[4]
                self.intro=item[5]
                self.lineEditID.setText(str(self.id))
                self.lineEditCode.setText(self.code)
                self.lineEditName.setText(self.name)
                self.lineEditAge.setText(str(self.age))
                self.lineEditIntro.setText(self.intro)
                #self.labelPicture.setPixmap(None)
                if self.avatar !=None:
                    imgdata = base64.b64decode(self.avatar)
                    pixmap = QPixmap()
                    pixmap.loadFromData(imgdata)
                    self.labelPicture.setPixmap(pixmap)
                else:
                    pixmap = QPixmap("images/ic_picture.png")
                    self.labelPicture.setPixmap(pixmap)
            else:
                print("Not Found")
            cursor.close()
        except:
            traceback.print_exc()
    def processbtnAvatar(self):
        filters = "Picture PNG (*.png);;All files(*)"
        filename, selected_filter = QFileDialog.getOpenFileName(self.MainWindow, filter=filters)
        if filename == '':
            return
        pixmap = QPixmap(filename)
        self.labelPicture.setPixmap(pixmap)

        with open(filename, "rb") as image_file:
            self.avatar = base64.b64encode(image_file.read())
            print(self.avatar)
        pass
    def processbtnRemoveAvatar(self):
        self.avatar = None
        pixmap = QPixmap(self.default_avatar)
        self.labelPicture.setPixmap(pixmap)
    '''def processbtnNew(self):
        pass
    def processbtnUpdate(self):
        pass
    def processbtnInsert(self):
        pass
    def processbtnRemove(self):
        pass'''
