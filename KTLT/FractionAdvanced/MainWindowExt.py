from PyQt6.QtWidgets import QMessageBox

from FractionAdvanced.MainWindow import Ui_MainWindow
from FractionAdvanced.model.Fraction import parse_fraction
from FractionAdvanced.model.Fractions import sort_fraction, quick_sort_fractions


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
        self.display_fractions = [] #Luu fraction duoi dang: a/b
        self.list_fraction = [] #Luu fraction duoi dang: [a,b]
    def show(self):
        self.MainWindow.show()
    def processSignalsAndSlot(self):
        self.pushButtonNew.clicked.connect(self.processNew)
        self.pushButtonSave.clicked.connect(self.processSave)
        self.pushButtonExit.clicked.connect(self.processExit)
        self.pushButtonRemove.clicked.connect(self.processRemove)
        self.pushButtonSort.clicked.connect(self.processSort)
        self.pushButtonFind.clicked.connect(self.processFind)
        self.listWidget.itemSelectionChanged.connect(self.print_listWidget)
    def processNew(self):
        self.lineEditInput.setText('')
        self.lineEditInput.setFocus()
    def processSave(self):
        fraction = self.lineEditInput.text()
        frc = parse_fraction(fraction) #frc = [a,b]
        if frc == False:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Warning')
            msgBox.setText('Valid Error!')
            msgBox.setInformativeText('Please enter again!')
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        self.list_fraction.append(frc)
        f = str(frc[0]) + "/" + str(frc[1])
        self.display_fractions.append(f)
        self.lineEditQuantity.setText(str(len(self.display_fractions)))
        self.listWidget.addItem(f)
    def processExit(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Xác nhận thoát')
        msgBox.setText('Bạn có chắc chắn muốn thoát không?')
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes |
                                  QMessageBox.StandardButton.No)
        rs = msgBox.exec()
        if rs == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
    def processRemove(self):
        current_row = self.listWidget.currentRow()
        if current_row >= 0:
            current_item = self.listWidget.takeItem(current_row)
            del current_item
    def print_listWidget(self):
        cur_row = self.listWidget.currentRow()
        cur_item = self.display_fractions[cur_row]
        self.lineEditInput.setText(cur_item)
    def processSort(self):
        if self.lineEditSortFrom.text() == '' or self.lineEditSortTo.text() =='':
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Warning')
            msgBox.setText('Valid Error!')
            msgBox.setInformativeText('Không được để trống phần Sort From và Sort To!!!')
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
        else:
            min = self.lineEditSortFrom.text()
            max = self.lineEditSortTo.text()
            list_sort = sort_fraction(self.list_fraction,min, max)
            for f in list_sort:
                item = str(f[0]) + "/" + str(f[1])
                self.listWidgetSort.addItem(item)
    def processFind(self):
        if self.lineEditInput.text() == '':
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Warning')
            msgBox.setText('Valid Error!')
            msgBox.setInformativeText('Xin vui lòng nhập phân số mà bạn muốn tìm vào ô Input!!!')
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
        else:
            f_find = self.lineEditInput.text()
            f = parse_fraction(f_find)
            rs = quick_sort_fractions(f, self.list_fraction,0, len(self.list_fraction))
            if rs == -1:
                msgBox = QMessageBox()
                msgBox.setWindowTitle('Information')
                msgBox.setText(f'Không tìm thấy phân số {f_find}')
                msgBox.setIcon(QMessageBox.Icon.Information)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle('Information')
                msgBox.setText(f'Đã tìm thấy phân số {f_find}')
                msgBox.setIcon(QMessageBox.Icon.Information)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
