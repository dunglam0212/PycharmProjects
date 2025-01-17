from math import log

def loga(a,x):
    y = log(x)/log(a) if (x>0) and (a>0) and (a!=1) else 'Giá trị không hợp lệ!'
    return y

flag = True
while flag:
    try:
        A = float(input('Nhập cơ số A: '))
        X = float(input('Nhập X: '))
        result = loga(A, X)
        print(result)
        flag = False
    except:
        print('Giá trị không hợp lệ!')





