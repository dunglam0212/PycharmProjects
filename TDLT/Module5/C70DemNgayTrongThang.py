'''Nhập vào 1 tháng, xuất tháng đó có bao nhiêu ngày.
1,3,5,7,8,10,12➔có 31 ngày
4,6,9,11➔có 30 ngày
Nếu là tháng 2 thì yêu cầu nhập thêm năm. Năm nhuần thì tháng 2 có 29 ngày,
không nhuần có 28 ngày
Nếu tháng không nằm trong [1..12] thì thông báo là không hợp lệ'''
'''Nháp:
m = int(input('Nhập tháng: '))
if m%2 != 0 and m != 9 and m != 11: #Nếu m là số lẻ khác 9 và 11 --> 31 ngày
    print(f'Tháng {m} có 31 ngày')
elif m == 9 or m == 11: #Nếu m=9 hoặc m =11 thì có 31 ngày
    print(f'Tháng {m} có 31 ngày')
elif m != 2: #m là số chẵn khác 2 --> 30 ngày
    print(f'Tháng {m} có 30 ngày')
else: #m=2 --> yêu cầu nhập thêm năm
    y = int(input('Vui lòng nhập năm: '))
    if (y%4 == 0 and y%100 != 0) or y%400 == 0: #Nếu là năm nhuần --> 29 ngày
        print(f'Tháng {m} năm {y} có 29 ngày')
    else: #Không phải năm nhuần --> 28 ngày
        print(f'Tháng {m} năm {y} có 28 ngày')'''


def check_pint(n):
    n = 'True' if n>0 else 'False'
    return n

def nam_nhuan(y):
    y = 'True' if (y%4 == 0 and y%100 != 0) or y%400 == 0 else 'False'
    return y

def dem_ngay(m):
    if m % 2 != 0 and m != 9 and m != 11:
        print(f'Tháng {m} có 31 ngày')
    elif m == 9 or m == 11:
        print(f'Tháng {m} có 31 ngày')
    elif m != 2:
        print(f'Tháng {m} có 30 ngày')
    else:
        flag1 = True
        while flag1:
            y = int(input('Nhập năm: '))
            rs1 = check_pint(y)
            if rs1 == 'True':
                result = nam_nhuan(y)
                if result == 'True':
                    print(f'Tháng {m} năm {y} có 29 ngày')
                    flag1 = False
                else:
                    print(f'Tháng {m} năm {y} có 28 ngày')
                    flag1 = False
            else:
                print('Vui lòng nhập năm là một số nguyên dương!')

flag = True
while flag:
    try:
        m = int(input('Nhập tháng: '))
        rs = check_pint(m)
        if rs == 'True':
            dem_ngay(m)
            flag = False
    except:
        print('Giá trị bạn nhập không hợp lệ!')


