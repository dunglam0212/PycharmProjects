import os
import traceback
import webbrowser

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog, QMessageBox

from DataStructure.QuanLySanPham2.io.FileFactory import FileFactory
from DataStructure.QuanLySanPham2.models.ListProduct import ListProduct
from DataStructure.QuanLySanPham2.models.Product import Product
from DataStructure.QuanLySanPham2.ui.MainWindowAboutExt import MainWindowAboutExt
from DataStructure.QuanLySanPham2.ui.MainWindowProduct import Ui_MainWindow


class MainWindowProductExt(Ui_MainWindow):
    def __init__(self):
        self.login_emp = None
        #tạo cơ sở giả lập
        #self.database_product = ListProduct().queryData()
        self.database_product = ListProduct()
        self.filefactory = FileFactory()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.statusbar.addWidget(self.labelWelcome)
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.actionIntroduction.triggered.connect(self.processIntroductionWindow)
        self.actionExit.triggered.connect(self.MainWindow.close)
        self.actionGuidlines.triggered.connect(self.processGuidlines)
        self.tableWidgetListProduct.itemSelectionChanged.connect(self.processitemSelectionChanged)
        self.pushButtonSave.clicked.connect(self.processSave)
        self.actionSaveFile.triggered.connect(self.processSaveFile)
        self.actionReadFile.triggered.connect(self.processReadFile)
        self.pushButtonEdit.clicked.connect(self.processEdit)
        self.pushButtonRemove.clicked.connect(self.processRemove)
    def show_login_infor(self):
        login_html_welcome = f"<font color='red'>Xin chào:</font> {self.login_emp.name}"
        self.labelWelcome.setText(login_html_welcome)
    def processIntroductionWindow(self):
        mainwindow=QMainWindow()
        self.aboutUi = MainWindowAboutExt()
        self.aboutUi.setupUi(mainwindow)
        self.aboutUi.show()
    def processGuidlines(self):
        #lấy đường dẫn hiện tại của phần mềm
        current_path = os.getcwd()
        file_help = f'{current_path}/../assests/Introduction.pdf'
        webbrowser.open_new(file_help)
    def print_product_in_qtable(self):
        try:
            #Xóa dữ liệu cũ đi:
            self.is_completed = False
            self.tableWidgetListProduct.setRowCount(0)
            for i in range(self.database_product.count()):
                product_i = self.database_product.get_product_by_index(i)
                #thêm 1 dòng mới vào qtable:
                self.tableWidgetListProduct.insertRow(i)
                column_id = QTableWidgetItem(str(product_i.id))
                column_name = QTableWidgetItem(str(product_i.name))
                column_quantity = QTableWidgetItem(str(product_i.quantity))
                if product_i.quantity < 5:
                    column_quantity.setForeground(Qt.GlobalColor.red)
                    column_quantity.setBackground(Qt.GlobalColor.yellow)
                column_price = QTableWidgetItem(str(product_i.price))
                self.tableWidgetListProduct.setItem(i, 0, column_id)
                self.tableWidgetListProduct.setItem(i, 1, column_name)
                self.tableWidgetListProduct.setItem(i, 2, column_quantity)
                self.tableWidgetListProduct.setItem(i, 3, column_price)
            self.is_completed = True
        except:
            traceback.print_exc()
    def processitemSelectionChanged(self):
        if self.is_completed == False:
            return
        #Xác định dòng mà khách hàng chọn trên giao diện
        row = self.tableWidgetListProduct.currentRow()
        column_id = self.tableWidgetListProduct.item(row,0)
        column_name = self.tableWidgetListProduct.item(row, 1)
        column_quantity = self.tableWidgetListProduct.item(row, 2)
        column_price = self.tableWidgetListProduct.item(row, 3)
        self.lineEditProductID.setText(column_id.text())
        self.lineEditProductName.setText(column_name.text())
        self.lineEditQuantity.setText(column_quantity.text())
        self.lineEditPrice.setText(column_price.text())

    def processSave(self):
        product_new = Product()
        product_new.id = self.lineEditProductID.text()
        product_new.name = self.lineEditProductName.text()
        product_new.quantity = int(self.lineEditQuantity.text())
        product_new.price = float(self.lineEditPrice.text())
        self.database_product.add_product(product_new)
        self.print_product_in_qtable()
    def processSaveFile(self):
        #Bản chất lưu file: xuất dữ liệu trong bộ nhớ (RAM-bộ nhớ tạm) xuống ổ cứng
        #để khi tắt phần mềm mở lại thì vẫn còn dữ liệu đã nạp trước đó
        try:
            file_filter = "Định dạng Json file (*.json);;Tất cả các loại file (*)"
            filename, selected_filter = QFileDialog.getSaveFileName(self.MainWindow, filter=file_filter)
            if filename=='':
                return
            print('Tên file mà bạn muốn lưu mới: ', filename)
            self.filefactory.writeData(filename, self.database_product.products)
            msgBox = QMessageBox()
            msgBox.setText(f'Đã xuất dữ liệu sang định dạng json thành công\n"'
                           f'Nơi xuất dữ liệu thành công [{filename}]')
            msgBox.setWindowTitle('Thông báo')
            msgBox.exec()
        except:
            traceback.print_exc()
    def processReadFile(self):
        #Bắt buộc dùng try, except để phòng trường hợp máy bị mất kết nối, rớt mạng
        try:
            file_filter = "Định dạng Json file (*.json);;Tất cả các loại file (*)"
            filename, selected_filter = QFileDialog.getOpenFileName(self.MainWindow, filter=file_filter)
            if filename=='':
                return
            products = self.filefactory.readData(filename, Product)
            self.database_product.products = products
            self.print_product_in_qtable()
        except:
            traceback.print_exc()
    def processEdit(self):
        try:
            product = self.database_product.find_product_by_id(self.lineEditProductID.text())
            if product == None:
                return
            product.name = self.lineEditProductName.text()
            product.quantity = int(self.lineEditQuantity.text())
            product.price = self.lineEditPrice.text()
            self.print_product_in_qtable()
        except:
            traceback.print_exc()
    def processRemove(self):
        msgBox = QMessageBox(self.MainWindow)
        msgBox.setWindowTitle('Confirmation')
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setText(f'Are you sure to remove the item has ID [{self.lineEditProductID.text()}]?')
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgBox.setStandardButtons(buttons)
        button = msgBox.exec()
        if button == QMessageBox.StandardButton.Yes:
            self.database_product.remove_product_by_id(self.lineEditProductID.text())
            self.print_product_in_qtable()
#Đề bài nho nhỏ:
'''Khi mở giao diện lên, chọn đại 1 sản phẩm và nó hiện lên phần chi tiết sản phẩm
Sau đó thoát phần mềm (kh ấn lưu hay bất kỳ nút nào khác nữa)
Thì khi mở lại thì giao diện vẫn hiện đúng thông tin của sản phẩm đó'''

