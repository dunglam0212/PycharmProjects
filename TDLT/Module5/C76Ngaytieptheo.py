#CHƯA HOÀN THIỆN
'''Sinh viên viết chương trình nhập vào 3 số nguyên là ngày, tháng, năm. Sau đó xuất
ra ngày kế sau của ngày vừa nhập này theo định dạng ngày/tháng/năm
Ví dụ:
- Nếu nhập 29/6/2024 thì ngày kế tiếp 30/6/2024
- Nếu nhập 30/6/2024 thì ngày kế tiếp là 1/7/2024
- Nếu nhập 31/12/2024 thì ngày kế tiếp là 1/1/2025
Hướng dẫn:
Sinh viên áp dụng cấu trúc if..elif lồng nhau để thực hiện. Lưu ý các ngày đặc biệt
đó là các ngày cuối tháng, cuối năm, và năm nhuần (vì khi năm nhuần thì tháng 2
có 29 ngày). Do đó cần phải xử lý hết các trường hợp đặc biệt này.'''

def next_day(d,m,y):
    if d==31 and m in (1,3,5,7,8,10):
        return f'1/{m+1}/{y}'
    elif d==31 and m==12:
        return f'1/1/{y+1}'
    elif d==30 and m in (4,6,9,11):
        return f'1/{m+1}/{y}'
    elif m==2:
        if (y%4==0 and y%100!=0) or y%400 == 0:
            if d==29:
                return f'1/3/{y}'
            elif d>29:
                return 'Giá trị bạn nhập không hợp lệ'
        else:
            if d==28:
                return f'1/3/{y}'
            elif d>28:
                return 'Giá trị bạn nhập không hợp lệ'
    else:
        return f'{d+1}/{m}/{y}'

def check_day(d):
    return 'False' if (d<0 or d>31) else 'True'

def check_month(m):
    return 'False' if (m<0 or m>12) else 'True'

flag = True
while flag:
    try:
        d = int(input('Nhập ngày: '))
        if check_day(d) == 'True':
            m = int(input('Nhập tháng: '))
            if check_month(m)=='True':
                y = int(input('Nhập năm: '))
                if y>0:
                    print(f'Ngày mà bạn vừa nhập là {d}/{m}/{y}')
                    print(f'Ngày tiếp theo là {next_day(d, m, y)}')
                    flag = False
                else:
                    print('Năm bạn nhập không đúng!')
            else:
                print('Tháng bạn nhập không hợp lệ!')
        else:
            print('Ngày bạn nhập không hợp lệ!')
    except:
        print('Giá trị bạn nhập không hợp lệ!')







