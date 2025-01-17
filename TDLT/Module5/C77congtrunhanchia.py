#CHƯA XỬ LÝ NGOẠI LỆ!!!!
'''Sinh viên viết lệnh để nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Sau đó
xuất kết quả theo đúng phép toán đã nhập. Ví dụ: Đầu vào a=5, b=3, và op= ‘+’ thì
kết quả xuất ra màn hình là: 5+3=8
Hướng dẫn:
Yêu cầu Sinh viên áp dụng match…case và kết hợp if…else để xử lý bài này. Bao
gồm lệnh try…except để xử lý khi người dùng cố tình nhập sai dữ liệu.'''

def tt(a,b,op):
    match op:
        case '+':
            return f'{a}+{b} = {a + b}'
        case '-':
            return f'{a}-{b} = {a - b}'
        case '*':
            return f'{a}*{b} = {a * b}'
        case '/':
            return f'{a}/{b} = {a / b}'
        case _:
            return 'Toán tử không hợp lệ!'

flag = True
while flag:
    try:
        a = float(input('Nhập số a: '))
        b = float(input('Nhập số b: '))
        op = input('Nhập toán tử: ')
        print(tt(a,b,op))
        flag = False
    except:
        print('Giá trị bạn nhập không hợp lệ!')