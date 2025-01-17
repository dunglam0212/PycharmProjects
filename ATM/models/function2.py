#Chức năng 2: Rút tiền
from models.ListCustomer import *


def rut_tien(index):
    if hanmuc[index] == 0:
        print('HẠN MỨC GIAO DỊCH TRONG NGÀY CỦA BẠN ĐÃ HẾT')
        return
    else:
        print('[0. Thoát]')
        while True:
            ruttien = input('NHẬP SỐ TIỀN CẦN RÚT: ')
            if ruttien == '0':
                break
            if ruttien.isdigit():
                if int(ruttien) > sodutk[index]:
                    print(f'KHÔNG ĐỦ TIỀN TRONG ATM ĐỂ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI VỚI SỐ TIỀN RÚT THẤP HƠN {sodung_atm}!!!')
                elif hanmuc[index] < int(ruttien):
                    print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI!!!')
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
