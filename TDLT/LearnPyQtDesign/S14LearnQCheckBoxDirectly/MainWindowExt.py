from PyQt6.QtCore import Qt

from LearnPyQtDesign.S14LearnQCheckBoxDirectly.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        # Mặc định là sẽ Checked QCheckbox
        self.checkBox.setChecked(True)
        self.checkBox.stateChanged.connect(self.processChecked)
    def show(self):
        self.MainWindow.show()
    def processChecked(self, value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            self.label.show()
        elif state == Qt.CheckState.Unchecked:
            self.label.hide()