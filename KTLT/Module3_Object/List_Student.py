class ListStudent:
    def __init__(self):
        self.list = [] #Khởi tạo 1 list để chứa danh sách sinh viên
    #Hàm thêm 1 sv vào cuối danh sách
    def append_student(self,st):
        self.list.append(st)
    #Hàm xuất toàn bộ danh sách sinh viên
    def print_students(self):
        for st in self.list:
            print(st)