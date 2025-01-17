def tinh_khlk(year, khlk, khn):
    for i in range(1,year+1):
        khlk = khlk - khn
        print(f'Khấu hao lũy kế năm thứ {i} là: {khlk}')

def ktra_nam():
    flag1 = True
    while flag1:
        try:
            x = int(input('Số năm trích khấu hao: '))
            if x>0:
                return x
            else:
                print('Vui lòng nhập năm là một số nguyên dương!')
        except:
            print('Giá trị bạn nhập không hợp lệ!')

def ktra_gia():
    flag1 = True
    while flag1:
        try:
            y = float(input('Nhập giá: '))
            if y>0:
                return y
            else:
                print('Xin hãy nhập một số thực dương!')
        except:
            print('Giá trị bạn nhập không hợp lệ!')

def ktra_cp():
    flag1 = True
    while flag1:
        try:
            y = float(input('Nhập chi phí: '))
            if y>=0:
                return y
            else:
                print('Xin hãy nhập một số thực dương!')
        except:
            print('Giá trị bạn nhập không hợp lệ!')

def main():
    n = ktra_nam()
    p = ktra_gia()
    print('Nếu không có chi phí thì nhập số 0')
    cp = ktra_cp()
    ng = p + cp
    print(f'Nguyên giá TSCĐ là: {ng}')
    khlk = ng
    khn = ng / n
    print(f'Mức trích khấu hao năm là: {khn}')
    print(f'Mức trích khấu hao tháng là: {khn / 12}')
    tinh_khlk(n, khlk, khn)

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


