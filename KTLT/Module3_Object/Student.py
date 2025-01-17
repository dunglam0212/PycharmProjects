class Student:
    #Hàm tự động thực thi khi đối tượng được cấp phát ô nhớ
    def __init__(self, id,name,age):
        self.id = id
        self.name = name
        self.age = age
    #Tự động thực thi khi xuất đối tượng ra màn hình
    def __str__(self):
        infor = f"{self.id}\t{self.name}\t{str(self.age)}"
        return infor
