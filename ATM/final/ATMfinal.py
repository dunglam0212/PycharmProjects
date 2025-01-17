import time

# giả sử list người dùng chỉ có 5 thành viên trong nhóm
tenkh = ['LÂM THÙY DUNG', 'PHAN HỒNG NGỌC', 'NGUYỄN HỒNG TÂM NHƯ', 'PHẠM THÁI HUỲNH HƯƠNG', 'HUỲNH VĂN VŨ']
tentk = ['dung','ngoc','nhu','huong','vu']
mk = [1234, 2345, 3456, 4567, 5678]
sodutk = [30000000, 40000000, 50000000, 60000000, 70000000] #số dư trong tài khoản cá nhân
hanmuc = [5000000, 10000000, 15000000, 20000000, 30000000] #Hạn mức tín dụng: Số tiền tối đa mà mỗi kh có thể giao dịch
# giả sử cây ATM có sẵn 10 triệu tiền mặt
sodung_atm = [10000000]

def sign_in():
    while True:
        name = input('NHẬP TÊN TÀI KHOẢN: ').lower()
        if name in tentk:
            index = tentk.index(name)
            dem = 1
            while dem <= 3:
                password = input('NHẬP MÃ PIN (KHÔNG ĐƯỢC NHẬP SAI QUÁ 3 LẦN): ')
                if password.isdigit():
                    if mk[index] == int(password):
                        print(f'CHÀO MỪNG {tenkh[index]} ĐẾN VỚI NGÂN HÀNG HOA ĐIỂM 10!')
                        return index
                    else:
                        print(f'MÃ PIN KHÔNG HỢP LỆ (CÒN {3 - dem} LẦN THỬ)')
                        dem += 1
                else:
                    print('MÃ PIN PHẢI BAO GỒM 4 CHỮ SỐ!')
                    print(f'MÃ PIN KHÔNG HỢP LỆ (CÒN {3 - dem} LẦN THỬ)')
                    dem +=1
            print('TÀI KHOẢN BỊ KHÓA TẠM THỜI VÌ BẠN NHẬP SAI MÃ PIN QUÁ 3 LẦN, VUI LÒNG CHỜ TRONG 5 GIÂY!')
            #đếm ngược  5 giây:
            for i in range(5, 0, -1):
                print(i, end ='\t')
                print()
                time.sleep(1)  # Wait for 1 second
        else:
            print('TÊN TÀI KHOẢN KHÔNG TỒN TẠI!')

#Chức năng 1: Tra cứu
def tra_cuu(index):
    print(f'CHỦ THẺ: {tenkh[index]} \nSỐ DƯ: {sodutk[index]} VNĐ \nHẠN MỨC GIAO DỊCH: {hanmuc[index]} VNĐ')

#Chức năng 2: Rút tiền
def rut_tien(index):
    if hanmuc[index] == 0:
        print('HẠN MỨC GIAO DỊCH TRONG NGÀY CỦA BẠN ĐÃ HẾT')
        return
    else:
        print('[0. Thoát]') #Nhập số 0 để thoát
        while True:
            ruttien = input('NHẬP SỐ TIỀN CẦN RÚT: ')
            if ruttien == '0':
                break
            if ruttien.isdigit():
                if int(ruttien) > sodung_atm[0]:
                    print(f'KHÔNG ĐỦ TIỀN TRONG ATM ĐỂ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI VỚI SỐ TIỀN RÚT THẤP HƠN {sodung_atm}!!!')
                elif hanmuc[index] < int(ruttien):
                    print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI!!!')
                elif int(ruttien) > sodutk[index]:
                    print(f'SỐ TIỀN TRONG TÀI KHOẢN KHÔNG ĐỦ ĐỂ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI VỚI SỐ TIỀN THẤP HƠN {sodutk}!!!')
                elif int(ruttien) % 50000 == 0:
                    sodutk[index] -= int(ruttien)
                    sodung_atm[0] -= int(ruttien)
                    hanmuc[index] -= int(ruttien)
                    print(f'BẠN ĐÃ RÚT {ruttien} VNĐ THÀNH CÔNG. SỐ DƯ CÒN LẠI: {sodutk[index]} VNĐ')
                    print('BẠN CÓ MUỐN NHẬN HÓA ĐƠN KHÔNG?\n1. Có\n2. Không')
                    while True:
                        bienlai = input('Chọn: ')
                        if bienlai == '1':
                            print("\n--- HÓA ĐƠN GIAO DỊCH ---")
                            print(f"TÊN TÀI KHOẢN: {tenkh[index]}")
                            print(f"SỐ TIỀN RÚT: {ruttien} VND")
                            print(f"SỐ DƯ TÀI KHOẢN: {sodutk[index]} VND")
                            print("CẢM ƠN BẠN ĐÃ SỬ DỤNG DỊCH VỤ!")
                            return
                        elif bienlai == '2':
                            print('GIAO DỊCH HOÀN THÀNH, XIN VUI LÒNG ĐỢI NHẬN TIỀN')
                            return
                        else:
                            print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                else:
                    print('SỐ TIỀN GIAO DỊCH PHẢI LÀ BỘI SỐ CỦA 50000 VNĐ, XIN VUI LÒNG THỬ LẠI!!!')
            else:
                print('SỐ TIỀN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI!!!')

#Chức năng 3: Chuyển tiền
def chuyen_tien(index):
    if hanmuc[index] == 0:
        print('HẠN MỨC GIAO DỊCH TRONG NGÀY CỦA BẠN ĐÃ HẾT')
        return
    else:
        print('[0. Thoát]')
        while True:
            stk = input('NHẬP SỐ TÀI KHOẢN BẠN MUỐN CHUYỂN TIỀN: ')
            if stk.isdigit():
                while True:
                    chuyentien = input('NHẬP SỐ TIỀN CẦN CHUYỂN: ')
                    if chuyentien == '0':
                        break
                    if chuyentien.isdigit():
                        if int(chuyentien) > sodung_atm[0]:
                                print('ATM KHÔNG ĐỦ SỐ DƯ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI!!!')
                        elif int(chuyentien) > hanmuc[index]:
                            print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI!!!')
                        elif int(chuyentien) > sodutk[index]:
                            print(f'SỐ TIỀN TRONG TÀI KHOẢN KHÔNG ĐỦ ĐỂ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI VỚI SỐ TIỀN THẤP HƠN {sodutk}!!!')
                        elif int(chuyentien) % 50000 != 0:
                            print('SỐ TIỀN GIAO DỊCH PHẢI LÀ BỘI SỐ CỦA 50000 VNĐ, XIN VUI LÒNG THỬ LẠI!!!')
                            return
                        else:
                            sodutk[index] -= int(chuyentien)
                            sodung_atm[0] -= int(chuyentien)
                            hanmuc[index] -= int(chuyentien)
                            print('BẠN CÓ MUỐN NHẬN HÓA ĐƠN KHÔNG?\n1. Có\n2. Không')
                            while True:
                                bienlai = input('Chọn: ')
                                if bienlai == '1':
                                    print('----BIÊN LAI CHUYỂN TIỀN----')
                                    print(f'SỐ TÀI KHOẢN NGƯỜI NHẬN: {stk}\nSỐ TIỀN ĐÃ CHUYỂN: {int(chuyentien)} VNĐ\nSỐ DƯ: {sodutk[index]} VNĐ')
                                    print('----------------------------')
                                    return
                                elif bienlai == '2':
                                    print('GIAO DỊCH HOÀN THÀNH')
                                    return
                                else:
                                    print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                    else:
                        print('SỐ TIỀN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI!!!')
            else:
                print('SỐ TÀI KHOẢN KHÔNG TỒN TẠI!')

#chức năng 4: Đổi mã PIN
def doi_mk(index):
    print('[0. Thoát]') #Nhập 0 để thoát
    while True:
        oldpin = input('NHẬP MÃ PIN CŨ: ')
        if oldpin.isdigit():
            if str(oldpin) == "0":
                print('CẢM ƠN BẠN ĐÃ SỬ DỤNG DỊCH VỤ!')
                break
            if int(oldpin) == mk[index]:
                while True:
                    newpin = input('NHẬP MÃ PIN MỚI: ')
                    if newpin.isdigit():
                        if len(str(newpin)) == 4:
                            while True:
                                newpin1 = input('NHẬP LẠI MÃ PIN MỚI: ')
                                if newpin1.isdigit():
                                    if str(newpin1) == "0":
                                        print(f'BẠN ĐÃ LỰA CHỌN 0 ĐỂ THOÁT!')
                                        print('BẠN SẼ ĐƯỢC CHUYỂN ĐẾN MÀN HÌNH CHÍNH!')
                                        return
                                    if str(newpin) == str(newpin1):
                                        mk[index] = int(newpin)
                                        print('BẠN ĐÃ THAY ĐỔI THÀNH CÔNG MÃ PIN')
                                        return
                                    else:
                                        print('MÃ PIN MỚI KHÔNG TRÙNG KHỚP, XIN VUI LÒNG THỬ LẠI')
                                else:
                                    print('MÃ PIN PHẢI LÀ CHỮ SỐ, XIN VUI LÒNG THỬ LẠI')
                        else:
                            print('MÃ PIN CHỈ BAO GỒM 4 CHỮ SỐ, XIN VUI LÒNG THỬ LẠI!')
                    else:
                        print('MÃ PIN PHẢI LÀ CHỮ SỐ, XIN VUI LÒNG THỬ LẠI')
            else:
                print('SAI MÃ PIN, XIN VUI LÒNG THỬ LẠI')
        else:
            print('MÃ PIN PHẢI LÀ CHỮ SỐ, XIN VUI LÒNG THỬ LẠI')

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
            if sodung_atm[0] <= 0:
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
            if sodung_atm[0] <= 0:
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