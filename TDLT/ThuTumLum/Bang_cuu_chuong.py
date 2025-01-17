#In bảng cửu chương từ bàn phím
'''N = int(input('Bạn muốn in bảng cửu chương nào? '))
while (N<=0) or (N>9):
    print('Thông tin bạn nhập không hợp lệ!')
    N = int(input('Xin vui lòng nhập lại, bạn muốn in bảng cửu chương mấy? '))
for i in range(1,11):
    p = i*N
    print(f'{N}*{i} = {p}')'''

#Dùng vòng lặp for
'''def bcc(n1):
    for i in range(1,11):
        result = n1*i
        print(f'{n1}*{i} = {result}')'''

#Dùng vòng lặp while
def bcc():
    for n in range(1,10):
        i = 1
        print(f'Bảng cửu chương {n}')
        while i<=9:
            result = n*i
            print(f'{n}*{i} = {result}')
            i+=1
bcc()


'''def operate():
    n2 = int(input('Bạn muốn in bảng cửu chương nào?: '))
    while (n2 <= 0) or (n2 > 9):
        print('Vui lòng nhập vào số nguyên thuộc khoảng [1,9]')
        n2 = int(input('Xin vui lòng nhập lại, bạn muốn in bảng cửu chương mấy? '))
    print(f'Bảng cửu chương của {n2} là: ')
    bcc(n2)
#Cho chạy lần đầu
operate()
#Lần 1 chạy xong thì mới hỏi là có muốn tiếp tục chương trình không
while True:
    users_choice = input('Bạn có muốn tiếp tục chương trình không? Y/N: ')
    if users_choice.upper() == 'Y':
        operate()
    elif users_choice.upper() == 'N':
        print('Chương trình đã kết thúc')
        break
    else:
        print('Vui lòng chọn Y để tiếp tục hoặc N để kết thúc chương trình: ')'''