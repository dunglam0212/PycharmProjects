def cv(r):
    return 2*pi*r
def dt(r):
    return pi*r*r

flag = True
while flag:
    pi = 3.14
    try:
        r = float(input('Nhập bán kính hình tròn: '))
        print(f'Chu vi hình tròn có bán kính r = {r} là:', cv(r))
        print(f'Diện tích hình tròn có bán kính r = {r} là:', dt(r))
        flag = False
    except:
        print('Giá trị bạn nhập vào không đúng!')
        a = input('Bạn có muốn tiếp tục chương trình không? Y/N: ')
        if a.lower() == 'n':
            print('Xin cảm ơn! Hẹn gặp lại bạn vào lần sau!')
            flag = False

