#bài chưa thêm phần hỏi ng dùng có tiếp tục sử dụng ctrinh hay không, với chưa tạo lệnh thoát cho ng dùng
#vd như khi ngta nhập điểm sai nhiều quá mà muốn thoát thì chưa có lệnh thoát mà ctrinh cứ chạy hòaiiiii
def dtb(t,l,h):
    dtb = (t+l+h)/3
    return round(dtb,2)

flag = True
while flag:
    try:
        t,l,h = eval(input('Nhập điểm môn Toán, Lý, Hóa: '))
        '''
        Hàm eval() được sử dụng để chuyển đổi đầu vào từ dạng chuỗi (do người dùng nhập vào)
        thành dạng các giá trị số, và nó còn có thể tách các giá trị đó ra để gán cho các biến
        toan, ly, hoa.
        VD: khi ng dùng nhập vào chuỗi "8,7.5,6.5", hàm eval(input()) sẽ hoạt động như sau:
        1. Chuyển chuỗi đầu vào thành tuple số học: Dấu phẩy ngăn cách giữa các số trong chuỗi
        sẽ giúp eval hiểu rằng ng dùng đang nhập vào một tuple (8,7.6,6.5)
        2. Gán giá trị cho các biến: eval sẽ gán giá trị 8 cho biến toan, 7.5 cho ly, và 6.5 cho hoa
        --> Kh thể đổi hàm eval() thanh float() được, vì:
        float() chỉ chấp nhận 1 giá trị duy nhất, mà ở đây có tới 3 gtri lận nên khum đc'''
        if t<=0:
            print('Giá trị bạn nhập không hợp lệ! Xin vui lòng thử lại')
        elif l<=0:
            print('Giá trị bạn nhập không hợp lệ! Xin vui lòng thử lại')
        elif h<=0:
            print('Giá trị bạn nhập không hợp lệ! Xin vui lòng thử lại')
        else:
            print('Điểm môn Toán:',t)
            print('Điểm môn Lý:',l)
            print('Điểm môn Hóa',h)
            print('Điểm trung bình của bạn là:', dtb(t,l,h))
            flag = False
    except:
        print('Giá trị bạn nhập không hợp lệ! Xin vui lòng thử lại')



