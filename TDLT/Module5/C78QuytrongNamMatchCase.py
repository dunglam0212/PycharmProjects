#CHƯA KIỂM TRA NGOẠI LỆ!!!
def quy(m):
    match m:
        case 1|2|3:
            return 'Quý I'
        case 4|5|6:
            return 'Quý II'
        case 7|8|9:
            return 'Quý III'
        case 10|11|12:
            return 'Quý IV'
        case _:
            return 'Giá trị bạn nhập không hợp lệ!'

flag = True
while flag:
    try:
        m = int(input('Nhập tháng: '))
        print(quy(m))
        flag = False
    except:
        print('Giá trị bạn nhập không hợp lệ!')