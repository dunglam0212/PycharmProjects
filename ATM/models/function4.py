#chức năng 4: Đổi mã PIN
from models.ListCustomer import mk

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
                                    if int(newpin1) == 0:
                                        pass
                                    if int(newpin) == int(newpin1):
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