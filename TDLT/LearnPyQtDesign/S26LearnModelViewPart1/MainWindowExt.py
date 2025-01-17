from LearnPyQtDesign.S26LearnModelViewPart1.Employee import Employee
from LearnPyQtDesign.S26LearnModelViewPart1.EmployeeModel import EmployeeModel
from LearnPyQtDesign.S26LearnModelViewPart1.FileFactory import FileFactory
from LearnPyQtDesign.S26LearnModelViewPart1.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.employees = []
        self.selectedEmployee = None
        # Lưu các biến đang được chọn trong giao diện QListView, dùng để xử lý lưu mới hoặc lưu cập nhật Employee
        self.fileFactory = FileFactory()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.model = EmployeeModel(self.employees)
        self.listView.setModel(self.model)
    def show(self):
        self.MainWindow.show()