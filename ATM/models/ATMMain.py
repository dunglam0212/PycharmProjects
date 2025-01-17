from ListCustomer import *
from models.function1 import tra_cuu
from models.function2 import rut_tien
from models.function3 import chuyen_tien
from models.function4 import doi_mk
from models.signin import sign_in

index = sign_in()
#Sau khi đăng nhập thành công, cho khách hàng chọn những tính năng của ATM:
#0. Thoát
#1. Tra cứu số dư tài khoản
#2. Rút tiền
#3. Chuyển tiền
#4. Thay đổi mã PIN
while True:
        print('#0. THOÁT\t#1. TRA CỨU SỐ DƯ\t#2. RÚT TIỀN\t#3. CHUYỂN TIỀN\t#4. THAY ĐỔI MÃ PIN')
        function = input('CHỌN CHỨC NĂNG MÀ BẠN MUỐN SỬ DỤNG: ')
        if function == '1':
            tra_cuu(index)
            print('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n1. Có\n2. Không')
            while True:
                q = input('Chọn: ')
                if q == '1':
                    print('BẠN SẼ ĐƯỢC CHUYỂN HƯỚNG ĐẾN MÀN HÌNH CHÍNH')
                    break
                elif q == '2':
                    print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
                    break
                else:
                    print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
        elif function == '2':
            if sodung_atm[index] <= 0:
                print('SỐ TIỀN TRONG ATM ĐÃ HẾT, BẠN KHÔNG THỂ SỬ DỤNG CHỨC NĂNG RÚT VÀ CHUYỂN TIỀN')
            else:
                rut_tien(index)
                print('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n1. Có\n2. Không')
                while True:
                    q = input('Chọn: ')
                    if q == '1':
                        print('BẠN SẼ ĐƯỢC CHUYỂN HƯỚNG ĐẾN MÀN HÌNH CHÍNH')
                        break
                    elif q == '2':
                        print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
                        break
                    else:
                        print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
        elif function == '3':
            if sodung_atm[index] <= 0:
                print('SỐ TIỀN TRONG ATM ĐÃ HẾT, BẠN KHÔNG THỂ SỬ DỤNG CHỨC NĂNG RÚT VÀ CHUYỂN TIỀN')
            else:
                chuyen_tien(index)
                print('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n1. Có\n2. Không')
                while True:
                    q = input('Chọn: ')
                    if q == '1':
                        print('BẠN SẼ ĐƯỢC CHUYỂN HƯỚNG ĐẾN MÀN HÌNH CHÍNH')
                        break
                    elif q == '2':
                        print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
                        break
                    else:
                        print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
        elif function == '4':
            doi_mk(index)
            print('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n1. Có\n2. Không')
            while True:
                q = input('Chọn: ')
                if q == '1':
                    print('BẠN SẼ ĐƯỢC CHUYỂN HƯỚNG ĐẾN MÀN HÌNH CHÍNH')
                    break
                elif q == '2':
                    print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
                    break
                else:
                    print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
        elif function == '0':
            print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
            break
        else:
            print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')