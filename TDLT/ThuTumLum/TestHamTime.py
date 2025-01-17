from datetime import datetime
from math import *
from random import randrange

ten = input("Hãy nhập tên của bạn: ")
z = eval("round((1*1374 - 43 + (-65/2) + cos(45) - sqrt(5)),3)")
batdau = datetime.now()
print("Hàm eval:",z)
print("Tên của bạn là:", ten)

x = int(input("Hãy nhập số bắt đầu: "))
y = int(input("Hãy nhật số kết thúc: "))
if x<=y:
    random= randrange(x,y)
    print("Số ngẫu nhiên từ x đến y là:", random)
else:
    exit() #Hàm dùng để thoát phần mềm
print("Kết quả random từ x đến y là:", random)

ketthuc = datetime.now()
thoigian = ketthuc - batdau
print("Chương trình chạy trong vòng: " + str(thoigian) + "giây")