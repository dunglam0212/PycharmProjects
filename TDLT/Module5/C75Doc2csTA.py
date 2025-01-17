'''Viết phương thức với đối số đầu vào là số có tối đa 2 chữ số. Hãy in ra cách đọc số
bằng tiếng Anh (ví dụ đọc số: 5: five, 11: eleven, 12: twelve, 15: fifteen, 20:
twenty, 35: thirty-five; 55: fifty-five; ….)'''
#CHƯA KIỂM TRA NGOẠI LỆ
def doc2cs_ta(x1,x2):
    if x1 == 0 and x2 == 0:
        return 'Zero'
    elif x1 == 0:
        x2 = doc_hang_dvi(x2)
        return f'{x2}'
    elif x1 == 1 and x2 == 0:
        return 'Ten'
    elif x1 == 1 and x2 == 1:
        return 'Eleven'
    elif x1 == 1 and x2 == 2:
        return 'Twelve'
    elif x1 == 1 and x2 == 3:
        return 'Thirteen'
    elif x1 == 1 and x2 == 5:
        return 'Fifteen'
    elif x1 == 1 and x2 == 8:
        return 'Eighteen'
    elif x1 == 1:
        x2 = doc_hang_dvi(x2)
        return f'{x2}teen'
    elif x1 == 2 and x2 == 0:
        return 'Twenty'
    elif x1 == 2:
        x2 = doc_hang_dvi(x2)
        return f'Twenty-{x2.lower()}'
    elif x1 ==3 and x2 == 0:
        return 'Thirty'
    elif x1 == 3:
        x2 = doc_hang_dvi(x2)
        return f'Thirty-{x2.lower()}'
    elif x1 ==5 and x2 ==0:
        return 'Fifty'
    elif x1 == 5:
        x2 = doc_hang_dvi(x2)
        return f'Fifty-{x2.lower()}'
    elif x1 == 8 and x2 == 0:
        return 'Eighty'
    elif x1 == 8:
        x2 = doc_hang_dvi(x2)
        return f'Eighty-{x2.lower()}'
    elif x2 == 0:
        x1 = doc_hang_dvi(x1)
        return f'{x1}ty'
    else:
        x1 = doc_hang_dvi(x1)
        x2 = doc_hang_dvi(x2)
        return f'{x1}ty-{x2.lower()}'

def doc_hang_dvi(x):
    if x==0:
        return ''
    elif x==1:
        return 'One'
    elif x==2:
        return 'Two'
    elif x==3:
        return 'Three'
    elif x==4:
        return 'Four'
    elif x==5:
        return 'Five'
    elif x==6:
        return 'Six'
    elif x==7:
        return 'Seven'
    elif x==8:
        return 'Eight'
    elif x==9:
        return 'Nine'
    else:
        return 'Value Error!'

flag = True
while flag:
    try:
        n = int(input('Nhập một số nguyên bất kỳ có 2 chữ số: '))
        n1 = n//10 #Lấy chữ số hàng chục
        n2 = n%10 #Lấy chữ số hàng đơn vị
        print(f'{n} đọc bằng chữ là: {doc2cs_ta(n1,n2)}')
        flag = False
    except:
        print('Giá trị bạn nhập không hợp lệ!')

