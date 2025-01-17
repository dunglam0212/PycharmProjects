#Chưa fix chữ số hàng đơn vị
def doc2cs_tv(x1,x2):
    if x1 == 1 and x2 ==1:
        return 'Mười một'
    elif x1 == 1:
        x2 = doc_hang_dvi(x2)
        return f'Mười {x2.lower()}'
    elif x1 == 5:
        x2 = doc_hang_dvi(x2)
        return f'Năm mươi {x2.lower()}'
    else:
        x1 = doc_hang_dvi(x1)
        x2 = doc_hang_dvi(x2)
        return f'{x1} mươi {x2.lower()}'

def doc_hang_dvi(x):
    if x==0:
        return ''
    elif x==1:
        return 'Mốt'
    elif x==2:
        return 'Hai'
    elif x==3:
        return 'Ba'
    elif x==4:
        return 'Bốn'
    elif x==5:
        return 'Lăm'
    elif x==6:
        return 'Sáu'
    elif x==7:
        return 'Bảy'
    elif x==8:
        return 'Tám'
    elif x==9:
        return 'Chín'
    else:
        return 'Giá trị bạn nhập không hợp lệ!'

flag = True
while flag:
    try:
        n = int(input('Nhập một số nguyên bất kỳ có 2 chữ số: '))
        n1 = n//10 #Lấy chữ số hàng chục
        n2 = n%10 #Lấy chữ số hàng đơn vị
        print(f'{n} đọc bằng chữ là: {doc2cs_tv(n1,n2)}')
        flag = False
    except:
        print('Giá trị bạn nhập không hợp lệ!')

