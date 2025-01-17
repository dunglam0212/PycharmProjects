'''def check_positive_integer():
    while True:
        try:
            num = int(input('Please enter the size of the diamond (a positive integer): '))
            if num > 0:
                return num
            else:
                print('This is not a positive integer! Please try again.')
        except ValueError:
            print('That is not a valid number! Please enter again.')

n = check_positive_integer()
print(n)'''

'''n = [3,6,9,12,24]
k = int(input('enter a number: '))
if k in n:
    print(k)
else:
    

#Vẽ hình chữ nhật
dong = 5
cot = 10
for i in range(dong):
    for j in range(cot):
        print('*', end=' ')
    print('')
'''

N=float(input("Nhập giá hàng: "))
k=float(input("Nhập lãi suất (%): "))
n=[3,6,9,12,24]
f=0
while True:
    m = int(input("Nhập số tháng muốn trả góp: "))
    if m in n:
        f= (N + m*N*k/100)/m
        print (f"Số tiền trả góp hàng tháng là {f}")
        break
    else:
        print ("Giá trị không hợp lệ, vui lòng nhập lại số tháng là 3,6,9,12,24 ")