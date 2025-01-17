def doc_2_chu_so_tv(x1,x2):
    match x1:
        case 0:
            match x2:
                case 1:
                    return 'Một'
                case 5:
                    return 'Năm'
                case _:
                    x2 = doc_hang_dvi(x2)
                    return f'{x2}'
        case 1:
            match x2:
                case 1:
                    return 'Mười Một'
                case _:
                    x2 = doc_hang_dvi(x2)
                    return f'Mười {x2.lower()}'
        case 5:
            x2 = doc_hang_dvi(x2)
            return f'Năm mươi {x2.lower()}'
        case _:
            x1 = doc_hang_dvi(x1)
            x2 = doc_hang_dvi(x2)
            return f'{x1} mươi {x2.lower()}'

def doc_hang_dvi(x):
    match x:
        case 0:
            return ''
        case 1:
            return 'Mốt'
        case 2:
            return 'Hai'
        case 3:
            return 'Ba'
        case 4:
            return 'Bốn'
        case 5:
            return 'Lăm'
        case 6:
            return 'Sáu'
        case 7:
            return 'Bảy'
        case 8:
            return 'Tám'
        case 9:
            return 'Chín'
        case _:
            return 'Giá trị bạn nhập không hợp lệ!'

flag = True
while flag:
    try:
        n = int(input('Nhập một số nguyên bất kỳ có 2 chữ số: '))
        n1 = n//10 #Lấy chữ số hàng chục
        n2 = n%10 #Lấy chữ số hàng đơn vị
        print(f'{n} đọc bằng chữ là: {doc_2_chu_so_tv(n1,n2)}')
        flag = False
    except:
        print('Giá trị bạn nhập không hợp lệ!')

