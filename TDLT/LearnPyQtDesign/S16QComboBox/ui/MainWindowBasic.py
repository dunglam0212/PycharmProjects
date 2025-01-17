import sys

from PyQt6.QtWidgets import QComboBox, QWidget, QVBoxLayout, QLabel, QApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Category Information')
        self.setMaximumWidth(300)

        #Create a grid layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        cb_label = QLabel('Please select a category: ', self)

        #Create a combobox
        self.cboCategory = QComboBox(self)
        self.cboCategory.addItem('Laptop')
        self.cboCategory.addItem('Phone & Tablet')
        self.cboCategory.addItem('Smart Watch')

        self.cboCategory.insertItem(1, 'Head Phone')
        self.cboCategory.insertItems(2, ['Mouse', 'Mouse Pad'])
        self.cboCategory.addItems(['Game & Stream', 'Monitor'])

        self.cboCategory.activated.connect(self.processSelectedCombobox)

        self.result_label  = QLabel('', self)

        layout.addWidget(cb_label)
        layout.addWidget(self.cboCategory)
        layout.addWidget(self.result_label)

        self.show()

    def processSelectedCombobox(self):
        index = self.cboCategory.currentIndex()
        text = self.cboCategory.currentText()
        self.result_label.setText(f'Your selected index = {index}, text = {text}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
