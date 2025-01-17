def ptb1(a,b):
    if a==0 and b==0:
        return 'Phương trình có vô số nghiệm'
    if a==0 and b!=0:
        return 'Phương trình vô nghiệm'
    else:
        return -b/a

flag = True
while flag:
    try:
        a = float(input('Nhập a: '))
        b = float(input('Nhập b: '))
        print(ptb1(a,b))
        flag = False
    except:
        print('Giá trị bạn nhập không hợp lệ!')


        
