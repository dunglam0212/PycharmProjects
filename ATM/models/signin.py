from models.ListCustomer import *
import time


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
                        print(f'CHÀO MỪNG {tenkh[index]} ĐẾN VỚI NGÂN HÀNG XYZ!')
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
