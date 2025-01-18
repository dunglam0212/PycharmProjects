# import functools
# import random
#
# from PyQt6.QtWidgets import QPushButton
#
# from Module2.C39InteractwithListApp.ui.MainWindow import Ui_MainWindow
#
#
# class MainWindowDemo(Ui_MainWindow):
#     def __init__(self):
#         self.list = []
#         self.previous_selected_button = None
#         self.selected_index = -1
#     def setupUi(self, MainWindow):
#         super().setupUi(MainWindow)
#         self.MainWindow = MainWindow
#         self.processSignalsAndSlot()
#     def show(self):
#         self.MainWindow.show()
#     def processSignalsAndSlot(self):
#         self.pushButtonCreateRandom.clicked.connect(self.processCreateRandom)
#         self.pushButtonDelete.clicked.connect(self.processDeleteSelectedButton)
#     def clearLayout(self, layout):
#         if layout is not None:
#             while layout.count():
#                 item = layout.takeAt(0)
#                 widget = item.widget()
#                 if widget is not None:
#                     widget.deleteLater()
#                 else:
#                     self.clearLayout(item.layout())
#     def CreateRandom(self):
#         self.clearLayout(self.verticalLayoutButtons)
#         for i in range(len(self.list)):
#             x = self.list[i]
#             title = f"{x}"
#             btn = QPushButton(text=title)
#             btn.setStyleSheet("background-color: rgb(188, 204, 220);")
#             self.verticalLayoutButtons.addWidget(btn)
#             btn.clicked.connect(functools.partial(self.ChangeBacgroundColor,i))
#     def ChangeBacgroundColor(self,i):
#         sender = self.MainWindow.sender()
#         if self.previous_selected_button != None: #ức là trước đó đã được chọn
#             self.previous_selected_button.setStyleSheet("background-color: rgb(188, 204, 220);")
#         sender.setStyleSheet("background-color: rgb(248, 250, 252);")
#         self.previous_selected_button = sender
#         #hiển thị lại dữ liệu của Button đang chọn trên lineedit
#         self.lineEditNumber.setText(sender.text())
#         self.selected_index = i
#     def processCreateRandom(self):
#         n = int(self.lineEditNumber.text())
#         self.list = [random.randrange(-100,101) for x in range(0,n)]
#         self.CreateRandom()
#     def processDeleteSelectedButton(self):
#         if self.selected_index == -1:
#             return
#         self.list.pop(self.selected_index)
#         self.selected_index = -1
#         self.previous_selected_button = None
#         self.lineEditNumber.setText('')
#         self.CreateRandom()
