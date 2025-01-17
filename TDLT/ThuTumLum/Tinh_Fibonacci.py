#Đề: Tính số hạng thứ N của dãy fibonacci
#Dãy Fibonacci là dãy vô hạn các số tự nhiên bắt đầu bằng hai phần tử 0 hoặc 1 và 1,
#các phần tử sau đó được thiết lập theo quy tắc mỗi phần tử luôn bằng tổng hai phần tử trước nó.
#Ở bài này sử dụng cách chuẩn là F(0) = 0 và F(1) = 1

'''#Cách 1:
N = int(input("Nhập vào một số nguyên dương N: "))
while N<=0:
    print('Thông tin bạn nhập không hợp lệ!')
    N = int(input('Xin vui lòng nhập vào 1 số nguyên dương N: '))
f_truoc_truoc = 0
f_truoc = 1
f_hien_tai = 1
i = 2
if N >= 2:
    while i <= N:
        f_hien_tai = f_truoc + f_truoc_truoc
        f_truoc_truoc = f_truoc
        f_truoc = f_hien_tai
        i = i + 1
    print(f'Số hạng thứ {N} = {f_hien_tai}')
else:
    print(f'Số hạng thứ {N} = 1')

#Đang muốn in ra dãy fibonacci đến số hạng thứ N => Done
def Fibonacci(N):
    fibo_list = [0, 1]
    for i in range(2, N+1):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    return fibo_list
N = int(input('Nhập vào số hạng thứ N: '))
while N <=0:
    print('Số hạng bạn nhập không hợp lệ!')
    N = int(input('Vui lòng nhập lại số hạng thứ N hợp lệ: '))
print(f'Dãy Fibonacci đến số hạng thứ {N} = {Fibonacci(N)}')
'''
#Đang muốn in ra màn hình số hạng thứ N của dãy Fibonacci
def so_hang(n1):
    fib_list = [0,1]
    for i in range(2, n1+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[n1]

def choice():
    n2 = int(input('Vui lòng nhập vào số hạng N mà bạn muốn in ra màn hình: '))
    while n2<0:
        print('Thông tin bạn nhập không hợp lệ!')
        n2 = int(input('Vui lòng nhập lại số hạng N mà bạn muốn in ra màn hình: '))
    if n2 == 0:
        print('Số hạng thứ 0 = 0')
    else:
        print(f'Số hạng thứ {n2} = {so_hang(n2)}')
#Cho chạy ctrinh lần đầu để kh bị hỏi là "Bạn có muốn tiếp tục kh" khi mới chạy ctrinh lần 1
choice()
#Sau khi so_hang() chạy lần 1 rồi thì mới hỏi là muốn tiếp tục ctrinh hay kh
flag = True
while flag:
    users_choice = input('Bạn có muốn tiếp tục chương trình không? Y/N: ')
    if users_choice.upper() == 'Y':
        choice()
    elif users_choice.upper() == 'N':
        print('Chương trình đã kết thúc')
        flag = False
    else:
        print('Xin vui lòng chọn Y (có) hoặc N (không): ')