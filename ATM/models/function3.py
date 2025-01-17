#Chức năng 3: Chuyển tiền
from models.ListCustomer import *

def chuyen_tien(index):
    if hanmuc[index] == 0:
        print('HẠN MỨC GIAO DỊCH TRONG NGÀY CỦA BẠN ĐÃ HẾT')
        return
    else:
        print('[0. Thoát]')
        while True:
            stk = input('NHẬP SỐ TÀI KHOẢN BẠN MUỐN CHUYỂN TIỀN: ')
            if stk != '0':
                if stk.isdigit():
                    while True:
                        chuyentien = input('NHẬP SỐ TIỀN CẦN CHUYỂN: ')
                        if chuyentien == '0':
                            break
                        if chuyentien.isdigit():
                            if int(chuyentien) > sodung_atm[0]:
                                print('ATM KHÔNG ĐỦ SỐ DƯ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI!!!')
                            elif int(chuyentien) <= sodutk[index]:
                                if hanmuc[index] < int(chuyentien):
                                    print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI!!!')
                                elif int(chuyentien) % 50000 != 0:
                                    print('SỐ TIỀN GIAO DỊCH PHẢI LÀ BỘI SỐ CỦA 50000 VNĐ, XIN VUI LÒNG THỬ LẠI!!!')
                                    pass
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
                                print('SỐ DƯ KHÔNG ĐỦ, XIN VUI LÒNG THỬ LẠI!!!')
                        else:
                            print('SỐ TIỀN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI!!!')
                else:
                    print('SỐ TÀI KHOẢN KHÔNG TỒN TẠI!')
            else:
                print('SỐ TÀI KHOẢN KHÔNG TỒN TẠI!')

