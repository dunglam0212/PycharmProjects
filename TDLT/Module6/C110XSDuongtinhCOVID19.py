def tinh_xs(a,b):
    '''a: Số người dương tính
    b: Số người khỏi bệnh trong a'''
    c = a - b
    p = (c*giai_thua(a-1))/giai_thua(a)
    return p

def giai_thua(n):
    gt = 1
    for i in range(n,0,-1):
        gt = gt*i
    return gt

def ktra_a():
    flag = True
    while flag:
        try:
            x = int(input('Nhập tổng số người bị dương tính: '))
            if x>0:
                return x
            else:
                print('Vui lòng nhập một số nguyên dương!')
        except:
            print('Giá trị bạn nhập không hợp lệ!')

def ktra_b():
    flag = True
    while flag:
        try:
            x = int(input('Hãy cho biết là bao nhiêu người đã khỏi bệnh: '))
            if x>=0:
                return x
            else:
                print('Vui lòng nhập một số nguyên dương!')
        except:
            print('Giá trị bạn nhập không hợp lệ!')

def main():
    flag = True
    while flag:
        a = ktra_a()
        b = ktra_b()
        if a>=b:
            rs = tinh_xs(a,b)
            print(f'Xác suất để người cuối cùng được chọn là dương tính với COVID-19 là: {rs}')
            flag = False
        else:
            print('Số người khỏi bệnh phải bé hơn hoặc bằng tổng số người bị dương tính!')

main()
Flag = True
while Flag:
    q = input('Bạn có muốn tiếp tục chương trình không? Y/N: ')
    if q.lower() == 'y':
        main()
    elif q.lower() == 'n':
        print('Cảm ơn bạn vì đã sử dụng chương trình!')
        Flag = False
    else:
        print('Vui lòng chọn Y hoặc N!')