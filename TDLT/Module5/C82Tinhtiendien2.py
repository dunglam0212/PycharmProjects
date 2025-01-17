'''Công ty điện lực Tia Chớp có nhu cầu xây dựng phần mềm tính tiền điện năm
2024. Cách tính tiền điện được mô tả dưới đây:
Gọi A là số ký điện cũ, B là số ký điện mới, C là số hộ dùng chung công tơ điện.
Phần mềm cần cung cấp 3 chức năng tính tiền điện như sau:
Giá sinh hoạt bậc thang(SHBT): Được tính theo 6 công thức
• Nếu B-A <= 50C, thanh toán: (B-A) * 1484
• Nếu B-A <=100C, thanh toán: (50C * 1484) + ((B-A) - 50C) * 1533
• Nếu B-A <=200C, thanh toán: (50C*1484) + (50C*1533) + ((B-A) - 100C)* 1786
• Nếu B-A <=300C, thanh toán: (50C*1484) + (50C*1533) + (100C*1786) + ((B-A) - 200C) * 2242
• Nếu B-A <=400C, thanh toán: (50C*1484) + (50C*1533) + (100C*1786) + (100C*2242) + ((B-A) - 300C) *2503
• Trường hợp còn lại, thanh toán: (50C*1484) + (50C*1533) + (100C*1786) + (100C*2242) + (100C*2503) + ((B-A) – 400C) * 2587
Giá kinh doanh: (B - A) * 2320
Giá sản xuất: (B - A) * 1518'''
#CHƯA KIỂM TRA NGOẠI LỆ!!!

def td_sh(a,b,c):
    if (b-a) <= (50*c):
        m = (b-a)*1484
        return m
    elif (b-a)<=(100*c):
        m = (50*c * 1484) + ((b-a)-50*c)*1533
        return m
    elif (b-a)<=(200*c):
        m = (50*c*1484) + (50*c*1533) + ((b-a) - 100*c)* 1786
        return m
    elif (b-a) <= (300*c):
        m = (50*c*1484) + (50*c*1533) + (100*c*1786) + ((b-a) - 200*c) * 2242
        return m
    elif (b-a) <= (400*c):
        m = (50*c*1484) + (50*c*1533) + (100*c*1786) + (100*c*2242) + ((b-a) - 300*c) *2503
        return m
    else:
        m = (50*c*1484) + (50*c*1533) + (100*c*1786) + (100*c*2242) + (100*c*2503) + ((b-a) - 400*c) * 2587
        return m

print('1. Sử dụng điện cho sinh hoạt')
print('2. Sử dụng điện cho kinh doanh')
print('3. Sử dụng điện cho sản xuất')
flag = True
while flag:
    try:
        T = input('Mục đích sử dụng điện? 1/2/3: ')
        if T == '1':
            A = float(input('Nhập số ký điện cũ: '))
            B = float(input('Nhập số ký điện mới: '))
            C = float(input('Số hộ dùng công tơ điện: '))
            print(f'Tiền điện phải trả là: {td_sh(A,B,C)} VNĐ')
            flag = False
        elif T == '2':
            A = float(input('Nhập số ký điện cũ: '))
            B = float(input('Nhập số ký điện mới: '))
            C = float(input('Số hộ dùng công tơ điện: '))
            m = (B - A) * 2320
            print(f'Tiền điện phải trả là: {m}VNĐ')
            flag = False
        elif T == '3':
            A = float(input('Nhập số ký điện cũ: '))
            B = float(input('Nhập số ký điện mới: '))
            C = float(input('Số hộ dùng công tơ điện: '))
            m = (B-A) * 1518
            print(f'Tiền điện phải trả là: {m} VNĐ')
            flag = False
        else:
            print('Vui lòng chọn 1,2 hoặc 3')
    except:
        print('Giá trị bạn nhập không hợp lệ!')