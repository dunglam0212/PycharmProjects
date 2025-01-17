from Module2.C27PhanMemToiUuChuoiDanhTu.Process import optimize_noun_string

string = "           trẦN      THanh     THẢN          "
rs = optimize_noun_string(string)
print('Chuỗi sau khi tối ưu chuỗi danh từ: ')
print(rs)

print(string.split())
print(' '.join(string.split()).lower().title())