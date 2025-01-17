from PyQt6.QtWidgets import QMessageBox
from PyQt6.uic.properties import QtWidgets

from final.ATMMainWindow import Ui_MainWindow

class ATMMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow


