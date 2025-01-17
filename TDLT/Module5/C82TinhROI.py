def roi(dt,cp):
    return (dt-cp)/cp

def invest(roi):
    match roi:
        case roi if roi >= 0.75:
            return 'nên đầu tư'
        case _:
            return 'không nên đầu tư'

flag = True
while flag:
    try:
        dt = float(input('Doanh thu của bạn là: '))
        if dt>=0:
            cp = float(input('Chi phí của bạn là: '))
            if cp>0: #Chi phí =0 thì kh tính đc ROI
                ROI = roi(dt,cp)
                print(f'Chỉ số ROI của bạn là {ROI}')
                print(f'Bạn {invest(ROI)}')
                flag = False
            else:
                print('Vui lòng nhập chi phí là một số dương')
        else:
            print('Vui lòng nhập doanh thu là một số không âm')
    except:
        print('Giá trị bạn nhập không hợp lệ!')