#Nhập từ bàn phím số nguyên dương N và tính tổng từ 1 đến N
N = int(input('Vui lòng nhập vào 1 số nguyên dương: '))
while N <=0:
    print('Thông tin bạn nhập không hợp lệ!')
    N = int(input('Vui lòng nhập lại 1 số N nguyên dương: '))
s = 0
i = 1
while i<=N:
    s = s + i
    i = i + 1
print(f'Tổng các số nguyên từ 1 đến {N} = {s}')
