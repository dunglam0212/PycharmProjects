from Module2.C38ListOperations.Process import create_list
from Module2.C39InteractwithListApp.ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.list = []
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.processSignalsAndSlot()
    def show(self):
        self.MainWindow.show()

    def processSignalsAndSlot(self):
        self.pushButtonCreateRandom.clicked.connect(self.processCreateRandom)
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
    def processCreateRandom(self):
        create_list(self.list)