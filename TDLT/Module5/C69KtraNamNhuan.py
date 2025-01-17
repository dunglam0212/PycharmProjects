'''Nhập vào một năm bất kỳ, kiểm tra năm đó có phải năm nhuần hay không. Biết
rằng: Năm nhuần là năm chia hết cho 4 nhưng không chia hết cho 100 hoặc chia
hết cho 400'''
def nam_nhuan(y):
    y = 'True' if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 'False'
    return y

flag = True
while flag:
    try:
        y = int(input('Nhập năm: '))
        if y>0:
            result = nam_nhuan(y)
            print(result)
            flag = False
        else:
            print('Xin vui lòng nhập năm là một số nguyên dương!')
    except:
        print('Giá trị bạn nhập không hợp lệ!')



