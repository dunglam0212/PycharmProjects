from PyQt6.QtWidgets import QInputDialog, QMessageBox

from LearnPyQtDesign.S17QListWidget.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonAdd.clicked.connect(self.processAdd)
        self.pushButtonUpdate.clicked.connect(self.processUpdate)
        self.pushButtonInsert.clicked.connect(self.processInsert)
        self.pushButtonRemove.clicked.connect(self.processRemove)
        self.pushButtonClear.clicked.connect(self.processClear)
        self.listWidget.itemClicked.connect(self.processitemClicked)
        self.listWidget.itemSelectionChanged.connect(self.processitemChanged)
        self.listWidget.itemDoubleClicked.connect(self.processUpdate)
    def show(self):
        self.MainWindow.show()
    def processAdd(self):
        text, ok = QInputDialog.getText(QInputDialog(), 'Add a new Data', 'New Data: ')
        if ok and text:
            self.listWidget.addItem(text)
    def processUpdate(self):
        current_row = self.listWidget.currentRow()
        if current_row >=0:
            item = self.listWidget.item(current_row)
            text, ok = QInputDialog.getText(QInputDialog(), 'Update Data', 'New Data: ', text = item.text())
            if ok and text:
                item.setText(text)
    def processInsert(self):
        current_row = self.listWidget.currentRow()
        if current_row >=0:
            text, ok = QInputDialog.getText(QInputDialog(), 'Insert New Item', 'New Data: ')
            if text and ok:
                self.listWidget.insertItem(current_row+1, text)
    def processRemove(self):
        current_row = self.listWidget.currentRow()
        if current_row >=0:
            item = self.listWidget.item(current_row)
            msg = QMessageBox()
            msg.setWindowTitle('Confirmation')
            msg.setText(f'Do you want to remove {item.text()}?')
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(QMessageBox.StandardButton.Yes |
                                   QMessageBox.StandardButton.No)
            rs = msg.exec()
            if rs == QMessageBox.StandardButton.Yes:
                current_item = self.listWidget.takeItem(current_row)
                del current_item
    def processClear(self):
        answer = QMessageBox.question(QMessageBox(),
                                      'Confirmation',
                                      'Do you want to clear all items?',
                                      QMessageBox.StandardButton.Yes |
                                      QMessageBox.StandardButton.No)
        if answer == QMessageBox.StandardButton.Yes:
            self.listWidget.clear()
    def processitemClicked(self):
        current_row = self.listWidget.currentRow()
        item = self.listWidget.item(current_row)
        self.MainWindow.setWindowTitle(item.text())
    def processitemChanged(self):
        current_row = self.listWidget.currentRow()
        item = self.listWidget.item(current_row)
        self.MainWindow.setWindowTitle(item.text())


