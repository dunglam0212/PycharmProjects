from math import sqrt

def do_dai(xa,ya,xb,yb):
    d = sqrt((xb-xa)**2 + (yb-ya)**2)
    return d

flag = True
while flag:
    try:
        xa,ya,xb,yb = eval(input('Nhập hoành độ và tung độ của điểm A và điểm B: '))
        print('Hoành độ điểm A:',xa)
        print('Tung độ điểm A:',ya)
        print('Hoành độ điểm B:',xb)
        print('Tung độ điểm B:',yb)
        print('Độ dài của đoạn thẳng AB =',do_dai(xa,ya,xb,yb))
        flag = False
    except:
        print('Giá trị bạn nhập không hợp lệ! Xin vui lòng thử lại')

