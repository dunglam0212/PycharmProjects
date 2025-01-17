x = 5
y = 'Hello'
z = 3 + 2.15j
t = True
a = 3.4

print(type(x))
print(type(t))
print(type(z))
print(z.imag + z.real)

import sys
print("Thong tin chi tiet cua int va float: ")
'''Chỉ kiểm tra thông tin cua int và float'''
print(sys.int_info)
print(sys.float_info)

del x
"""del dùng để xóa biến, các câu lệnh chứa biến x ở trc lệnh del thì vẫn chạy như bth,
          nhưng, các câu lệnh sau lệnh del thì không chạy được, bị lỗi"""
print(type(x))

