from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QMovie

from LearnPyQtDesign.S11LearnQLabelBasicWidgets.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        #Signals And Slot:
        self.pushButtonChangeText.clicked.connect(self.processChangeText)
        self.pushButtonFontSize.clicked.connect(self.processFontSize)
        self.pushButtonLeft.clicked.connect(self.processAlignLeft)
        self.pushButtonCenter.clicked.connect(self.processAlignCenter)
        self.pushButtonRight.clicked.connect(self.processAlignRight)
        self.pushButton.clicked.connect(self.processChangepngFormat)
        self.pushButton_2.clicked.connect(self.processChangegifFormat)
    def show(self):
        self.MainWindow.show()
    def processChangeText(self):
        self.labelName.setText("https://tranduythanh.com")
    def processFontSize(self):
        #get font object
        font = self.labelName.font()
        #change font size
        font.setPointSize(20)
        #set italic
        font.setItalic(True)
        #set bold
        font.setBold(True)
        #set font name
        font.setFamily('Times New Roman')
        #re-assign font
        self.labelName.setFont(font)
    def processAlignLeft(self):
        self.labelName.setAlignment(Qt.AlignmentFlag.AlignLeft)
    def processAlignCenter(self):
        self.labelName.setAlignment(Qt.AlignmentFlag.AlignCenter)
    def processAlignRight(self):
        self.labelName.setAlignment(Qt.AlignmentFlag.AlignRight)
    def processChangepngFormat(self):
        #create QPixmap instance
        pixmap = QPixmap('images/204-LÂM THÙY DUNG-TRƯỜNG ĐẠI HỌC KINH TẾ - LUẬT ĐHQG TP.HCM.png')
        #set pixmap for label
        self.label.setPixmap(pixmap)
    def processChangegifFormat(self):
        movie = QMovie('images/09-57-33-900_512.gif')
        self.label.setMovie(movie)
        movie.start()
