from PyQt6.QtCore import QAbstractListModel, Qt


class EmployeeModel(QAbstractListModel):
    def __init__(self, employees=None):
        super().__init__()
        self.employees = employees
        #Khởi tạo các biến ban đầu cho model, ở đây nhận vào 1 danh sách Employê
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            emp=self.employees[index.row()]
            return str(emp)
        #2 đối số: indẽ là vị trí của dòng dữ liệu sẽ hiển thị trên QListView
        #index.row() trả về integer tương ứng trong ds employees
        #DisplayRole là enum dùng để hiển thị dữ liệu, str(emp) để tự động gọi hàm __str__ trong lớp Employee.py
    def rowCount(self, index):
        return len(self.employees)
    #Trả về số phần tử trong danh sách
