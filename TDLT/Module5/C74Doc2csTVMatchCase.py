def doc_hang_chuc(x):
    match x:
        case 1:
            return 'Mười'
        case 2:
            return 'Hai mươi'
        case 3:
            return 'Ba mươi'
        case 4:
            return 'Bốn mươi'
        case 5:
            return 'Năm mươi'
        case 6:
            return 'Sáu mươi'
        case 7:
            return 'Bảy mươi'
        case 8:
            return 'Tám mươi'
        case 9:
            return 'Chín mươi'
        case _:
            return 'Giá trị bạn nhập không hợp lệ!'

def doc_hang_dvi(x):
    match x:
        case 1:
            return 'Một'
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

n = int(input('Nhập một số nguyên bất kỳ có 2 chữ số: '))
n1 = n//10 #Lấy chữ số hàng chục
n2 = n%10 #Lấy chữ số hàng đơn vị
n1 = doc_hang_chuc(n1)
n2 = doc_hang_dvi(n2)
print(f'{n} đọc bằng chữ là: {n1} {n2}')
