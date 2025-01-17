def nam_nhuan(y):
    y = 'True' if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 'False'
    return y

def dem_ngay(m):
    match m:
        case 1|3|5|7|8|10|12:
            return f'Tháng {m} có 31 ngày'
        case 4|6|9|11:
            return f'Tháng {m} có 30 ngày'
        case 2:
            y = int(input('Nhập năm: '))
            if y>0:
                result = nam_nhuan(y)
                if result == 'True':
                    return f'Tháng {m} năm {y} có 29 ngày'
                else:
                    return f'Tháng {m} năm {y} có 28 ngày'
        case _:
            return 'Giá trị không hợp lệ!'

flag = True
while flag:
    try:
        m = int(input('Nhập tháng: '))
        print(dem_ngay(m))
        flag = False
    except:
        print('Giá trị bạn nhập không hợp lệ!')

