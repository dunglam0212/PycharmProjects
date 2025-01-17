from DataStructure.QuanLyKhachHang.models.Customer import Customer
from DataStructure.QuanLyKhachHang.models.TypeCustomer import TypeCustomer

c1=Customer('c1','Obama','obama@gmail.com','0923846542',28,TypeCustomer.VIP) #Thêm () để chạy vào hàm init
print(c1) #Tự động thực hiện hàm __str__ trả về chuỗi đối tượng

c2=Customer() #Khởi tạo cho đối tượng chưa có thông tin, cả tháng sau mới biết thtin thì nhập sau
c2.id='c2'
c2.name='Putin'
c2.email='Putin@gmail.com'
c2.phone='0987654326'
c2.age=35
c2.tc=TypeCustomer.POTENTIAL
print(c2)