from math import *
from random import randrange

a = 9
print("Căn bậc hai của 9 =", sqrt(a))
print("9 mũ 2 =", pow(a,2))
print("9 mũ 2 =", a**2)
goc = 45
print("sin của góc 45 độ =", sin(radians(goc)))
print("cos của góc 45 độ =", cos(radians(goc)))
print("tan của góc 45 độ =", tan(radians(goc)))
print("cotan của góc 45 độ =", 1/(tan(radians(goc))))
print("Làm tròn 2 chữ số thập phân của sin(45)=", round(sin(radians(goc)),2))

b = 10
c = b-a
print("Trị tuyệt đối của b-a=", fabs(c))
d=1780
print("Làm tròn đến chữ số hàng chục của 1780=", round(d,1))
#Không có hàm làm tròn đến chữ số hàng chục, hàng trăm, hàng nghìn à?

x = int(input("Hãy nhập số bắt đầu: "))
y = int(input("Hãy nhật số kết thúc: "))
if x<=y:
    random= randrange(x,y)
    print("Số ngẫu nhiên từ x đến y là:", random)
else:
    exit() #Hàm dùng để thoát phần mềm
print("Kết quả random từ x đến y là:", random)

z = eval("round((1*1374 - 43 + (-65/2) + cos(45) - sqrt(5)),3)")
print("Hàm eval:",z)

