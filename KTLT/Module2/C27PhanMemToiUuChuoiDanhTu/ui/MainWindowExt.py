from PyQt6.QtWidgets import QMessageBox

from Module2.C27PhanMemToiUuChuoiDanhTu.Process import optimize_noun_string
from Module2.C27PhanMemToiUuChuoiDanhTu.ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonExit.clicked.connect(self.processExit)
        self.pushButtonNew.clicked.connect(self.processNew)
        self.pushButtonOptimize.clicked.connect(self.processOptimize)
    def processExit(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Confirmation")
        msgBox.setText("Do you want to exit?")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes|
                                  QMessageBox.StandardButton.No)
        msgBox.setIcon(QMessageBox.Icon.Question)
        rs = msgBox.exec()
        if rs == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
    def processNew(self):
        self.lineEditInput.setText('')
        self.lineEditOutput.setText('')
        self.lineEditInput.setFocus()
    def processOptimize(self):
        if self.lineEditInput.text() == '':
            dlg = QMessageBox()
            dlg.setWindowTitle("Warning")
            dlg.setText("Valid Error")
            dlg.setInformativeText("Please enter an input string!")
            dlg.setDefaultButton(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
        else:
            input_string = self.lineEditInput.text()
            output_string = optimize_noun_string(input_string)
            self.lineEditOutput.setText(output_string)