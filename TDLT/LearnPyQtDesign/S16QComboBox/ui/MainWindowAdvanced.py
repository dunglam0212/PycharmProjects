import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QApplication

from LearnPyQtDesign.S16QComboBox.Category import Category


class MainWindowAdvanced(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Lam Thuy Dung')
        self.setMinimumWidth(300)

        #create a grid layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        cb_label = QLabel('Please select a category: ', self)

        #create a combobox:
        self.cboCategory = QComboBox(self)

        laptop_icon = QIcon('images/iconlaptop.png')
        laptop_model = Category(100, 'Laptop')
        self.cboCategory.addItem(laptop_icon, laptop_model.name, laptop_model)

        phone_icon = QIcon("images/iconphone.png")
        phone_model = Category(200, "Phone")
        self.cboCategory.addItem(phone_icon, phone_model.name, phone_model)

        smart_icon = QIcon("images/iconsmartwatch.png")
        smart_model = Category(300, "Smart Watch")
        self.cboCategory.addItem(smart_icon, smart_model.name, smart_model)

        self.cboCategory.activated.connect(self.processSelectedCombobox)

        self.result_label = QLabel('', self)

        layout.addWidget(cb_label)
        layout.addWidget(self.cboCategory)
        layout.addWidget(self.result_label)

        self.show()
    def processSelectedCombobox(self):
        data = self.cboCategory.currentData()
        self.result_label.setText(f'Your selected index = {data}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindowAdvanced()
    sys.exit(app.exec())