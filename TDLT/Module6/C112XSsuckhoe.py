def xs_sk(a,b,c):
    a = a/100
    b = b/100
    c = c/100
    #Tính % người không đi khám sức khỏe:
    d = 1 - a
    xs = a*b + d*c
    return xs

def ktra_x():
    flag = True
    while flag:
        try:
            x = int(input('Phần trăm người dân đi khám sức khỏe định kỳ là: '))
            if 0<x<=100:
                return x
            else:
                print(f'Vui lòng nhập một số nguyên trong khoảng [1,100]!')
        except:
            print('Giá trị bạn nhập không hợp lệ!')

def ktra_y():
    flag = True
    while flag:
        try:
            y = int(input('Trong số người đi khám sức khỏe định kỳ, số người không có vấn đề sức khỏe ở năm kế tiếp là bao nhiêu phần trăm?: '))
            if 0<y<=100:
                return y
            else:
                print(f'Vui lòng nhập một số nguyên trong khoảng [1,100]!')
        except:
            print('Giá trị bạn nhập không hợp lệ!')

def ktra_z():
    flag = True
    while flag:
        try:
            z = int(input('Trong số người không đi khám sức khỏe định kỳ, số người không có vấn đề sức khỏe ở năm kế tiếp là bao nhiêu phần trăm?: '))
            if 0<z<=100:
                return z
            else:
                print(f'Vui lòng nhập một số nguyên trong khoảng [1,100]!')
        except:
            print('Giá trị bạn nhập không hợp lệ!')

def main():
    a = ktra_x()
    b = ktra_y()
    c = ktra_z()
    rs = xs_sk(a,b,c)
    print(f'Xác suất khi chọn ngẫu nhiên một người không có vấn đề về sức khỏe ở năm kế tiếp là: {rs}')

main()
Flag = True
while Flag:
    q = input('Bạn có muốn tiếp tục chương trình không? Y/N: ')
    if q.lower() == 'y':
        main()
    elif q.lower() == 'n':
        print('Cảm ơn bạn vì đã sử dụng chương trình!')
        Flag = False
    else:
        print('Vui lòng chọn Y hoặc N!')