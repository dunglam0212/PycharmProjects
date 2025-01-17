#Giả sử ng dùng nhập vào 1 danh sách gồm 5 phân số
from CalculateWithFractions.process.Fractions import *

#
# n = 3
# list_fractionss = []
# for i in range(n):
#     f = input("Please enter a fraction with type 'a/b': ")
#     parts = parse_fraction(f)
#     fraction = str(parts[0]) + "/" + str(parts[1])
#     print(fraction)
#     list_fractionss.append(parts)
#
# print(list_fractionss)

f_find = "34/67"
rs = find_fraction_in_list_fractions(f_find)
if rs == True:
    print(f'Đã tìm thấy phân số {f_find}!')
else:
    print(f'Tìm mỏi mắt cũng kh thấy phân số {f_find}!')

f_add = "1/5"
rs = add_fraction_to_list_fractions(f_add)
print(rs)

f_remove = "34/67"
rs = remove_fraction_from_list_fractions(f_remove)
if rs == True:
    print(f'Xoá thành công phân số {f_remove}')
    print('Danh sách phân số sau khi xoá là: ')
    print(list_fractions)
else:
    print(f'Không tìm thấy phân số {f_remove} để xoá!')

#thử sửa trực tiếp
f = "4/5"
f_change = parse_fraction(f)
list_fractions[3] = f_change
print(list_fractions)

list_fractions_float = []
for f in list_fractions:
    fraction = round(f[0]/f[1],5)
    list_fractions_float.append(fraction)
print(list_fractions_float)


min_fraction = "3/4"
max_fraction = "10/2"
rs = sort_fraction(min_fraction, max_fraction)
print(f'Các phân số thuộc đoạn [{min_fraction},{max_fraction}] là: ')
print(rs)

print('Danh sách phân số tăng dần là: ')
print(sort_ascending(list_fractions))

print('Danh sách phân số giảm dần là: ')
print(sort_descending(list_fractions))