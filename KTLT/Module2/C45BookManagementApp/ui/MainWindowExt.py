import functools

from PyQt6.QtWidgets import QPushButton

from Module2.C45BookManagementApp.ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.books = []
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonSave.clicked.connect(self.processSave)
    def processSave(self):
        book = {"ISBN":self.lineEditISBN.text(),
                "Title":self.lineEditTitle.text(),
                "Author":self.lineEditAuthor.text(),
                "Year":self.lineEditYear.text(),
                "Publisher":self.lineEditPublisher.text()}
        self.books.append(book)
        self.view_ui()
    def view_ui(self):
        #Xoá toàn bộ sách trong layout đi để nạp lại:
        self.clearLayout(self.verticalLayoutButtons)
        for i in range(len(self.books)):
            book = self.books[i]
            book_button = QPushButton(text=book["Title"])
            book_button.setStyleSheet("background-color: rgb(188, 204, 220);")
            self.verticalLayoutButtons.addWidget(book_button)
            book_button.clicked.connect(functools.partial(self.view_details,i))
    def view_details(self,i):
        book = self.books[i]
        self.lineEditISBN.setText(book["ISBN"])
        self.lineEditTitle.setText(book["Title"])
        self.lineEditAuthor.setText(book["Author"])
        self.lineEditYear.setText(book["Year"])
        self.lineEditPublisher.setText(book["Publisher"])
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())