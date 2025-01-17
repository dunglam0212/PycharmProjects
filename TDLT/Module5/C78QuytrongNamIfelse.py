'''Yêu cầu:
Sinh viên viết lệnh để nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong
năm. Nếu tháng nhập không hợp lệ thì cần thông báo lỗi
Hướng dẫn:
Yêu cầu Sinh viên áp dụng match…case và kết hợp if…else để xử lý bài này. Bao
gồm lệnh try…except để kiểm tra và thông báo lỗi.
Yêu cầu viết hàm đối với bài này, thử nghiệm với nhiều tháng khác nhau'''

def quy(m):
    if m in (1,2,3):
        return 'Quý I'
    elif m in (4,5,6):
        return 'Quý II'
    elif m in (7,8,9):
        return 'Quý III'
    elif m in (10,11,12):
        return 'Quý IV'
    else:
        return 'Giá trị bạn nhập không hợp lệ!'

flag = True
while flag:
    try:
        m = int(input('Nhập tháng: '))
        print(quy(m))
        flag = False
    except:
        print('Giá trị bạn nhập không hợp lệ!')