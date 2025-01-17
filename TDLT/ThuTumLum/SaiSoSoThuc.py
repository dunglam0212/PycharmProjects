'''a = 3.33 - 2.11
b = 10.44 - 9.22
if a == b:
    print("a và b bằng nhau")
else: print("a và b không bằng nhau")

a = 3.33 - 2.11
b = 10.44 - 9.22
epsilon = 0.00001 #Chọn 1 ngưỡng sai số để so sánh
if abs(a-b)<epsilon:
    print("a và b bằng nhau")
else: print("a và b không bằng nhau")

a = 3.33 - 2.11
b = 10.44 - 9.22
if round(a,6) == round(b,6): #Sử dụng hàm làm tròn round()
    print("a và b bằng nhau")
else: print("a và b không bằng nhau")'''


#Sử dụng 1 ngưỡng sai số để so sánh
a = 6.78 - 3.21
b = 10.89 - 7.32
x = 0.000001
if abs(a-b)<x:
    print("a và b bằng nhau")
else: print("a và b không bằng nhau")

#Sử dụng hàm làm tròn round()
a = 6.78 - 3.21
b = 10.89 - 7.32
if round(a,6) == round(b,6):
    print("a và b bằng nhau")
else: print("a và b không bằng nhau")