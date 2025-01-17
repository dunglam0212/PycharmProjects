from cmath import sqrt

def ptb2(a,b,c):
    if a==0:
        if b==0 and c==0:
            return 'Phương trình có vô số nghiệm'
        elif b==0 and c!=0:
            return 'Phương trình vô nghiệm'
        else:
            return -b/a
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            return 'Phương trình vô nghiệm'
        elif delta == 0:
            return f'Phương trình có nghiệm duy nhất là x = {-b/(2*a)}'
        else:
            x1 = (-b + sqrt(delta) / (2 * a))
            x2 = (-b - sqrt(delta) / (2 * a))
            return f'Phương trình có hai nghiệm lần lượt là {x1},{x2}'
flag = True
while flag:
    try:
        a = float(input('Nhập a: '))
        b = float(input('Nhập b: '))
        c = float(input('Nhập c: '))
        print(ptb2(a,b,c))
        flag = False
    except:
        print('Giá trị bạn nhập không hợp lệ!')
