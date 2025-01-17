x = 12
y = 7
print(f"{x}/{y}=",x/y)
print("x/y=", x/y)
#tạm thời thì hiểu cái f{} là muốn lấy dữ liệu gán của biến chứ không hiện chữ là x và y
print(f"{x}//{y}=",x//y)
#//: chia lấy phần nguyên
print(f"{x}%{y}=",x%y)
#%: chia lấy phần dư
print("2^3=", 2**3)
#**: lũy thừa

a = 7
a+=2 #a=a+2
print("Cộng và gán:",a)
a-=2 #a=a-2
print("Trừ và gán:",a)
a*=2 #a=a*2
print("Nhân và gán:",a)
a/=2 #a=a/2
print("Chia và gán:",a)
a//=2 #a=a//2
print("Chia lấy phần nguyên và gán:",a)
a%=2 #a=a%2
print("Chia lấy phần dư và gán:",a)
a**=2 #a=a**2
print("Lũy thừa và gán:",a)

print(a!=10)
print(not a!=10)
print(a is x)
print(a is not x)
if not a!=10 and x!=10:
    print("True")
else: print("False")

if not a!=10 or x!=10:
    print("True")
else: print("False")

if not a!=10 and x!=10 or y!=10:
    """Nếu như a=10 và x khác 10 hoặc y khác 10 =>True
    Ngược lại, a khác 10 và x=10 hoặc y=10 => False
    Có thể thấy, mặc dù not a!=10 sai, nhưng do y!=10 đúng => True"""
    print("True")
else: print("False")

if not a!=10 and x!=10 or y==10:
    """Vì not a!=10 v y==10 đều sai - 2 vế của or đều sai => False"""
    print("True")
else: print("False")