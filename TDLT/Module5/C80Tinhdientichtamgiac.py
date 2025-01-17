from math import sqrt

def cv(a,b,c):
    return a+b+c

def dttg(a,b,c):
    p = cv(a,b,c)/2
    dt = sqrt(p*(p-a)*(p-b)*(p-c))
    return dt

flag = True
while flag:
    try:
        a = float(input('Nhập độ dài cạnh thứ nhất: '))
        b = float(input('Nhập độ dài cạnh thứ hai: '))
        c = float(input('Nhập độ dài cạnh thứ ba: '))
        if (a<=0 or b<=0 or c<=0) or (a+b)<=c or (a+c)<=b or (b+c)<=a:
            print('Tam giác không hợp lệ!')
        else:
            print(f'Diện tích tam giác là: {dttg(a,b,c)}')
            flag = False
    except:
        print('Giá trị bạn nhập không hợp lệ')