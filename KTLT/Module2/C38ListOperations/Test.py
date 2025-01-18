from Module2.C38ListOperations.Process import *

list = [-66, -30, 6, 86, -13, 77, 28, -24, 30, -16]
# for i in range(10):
#     x = randint(-100,101)
#     list.append(x)
# print("Danh sách các phần tử trong List: ")
# print(list)
k=-16
rs = check_frequency(k, list)
print(f"Số lần xuất hiện của {k} là: {rs}")

n=17
rs1 = check_perfect_number(n)
if rs1 == True:
    print(f"{n} là số hoàn thiện")
else:
    print(f"{n} kh là số hoàn thiện")

rs2 = sum_perfect_number(list)
print(f"Tổng các số hoàn thiện trong List trên là: {rs2}")

rs3 = sort_asc(list)
print("Danh sách sau khi sắp xếp tăng dần là:")
print(rs3)

rs4 = sort_desc(list)
print("Danh sách sau khi sắp xếp giảm dần là:")
print(rs4)

itm_remove = 567
rs5 = remove_an_element(itm_remove, list)
if rs5 == True:
    print(f"Đã xoá thành công phần tử {itm_remove} trong danh sách")
    print(f"Danh sách sau khi xoá phần tử {itm_remove} là:")
    print(list)
else:
    print(f"Không tìm thấy phần tử {itm_remove} để xoá")
    print(f"Xoá phần tử {itm_remove} thất bại")

rs6 = remove_neg_numbers(list)
print(f"Danh sách sau khi xoá các số âm là: ")
print(rs6)

rs7 = remove_all(list)
print(f"Danh sách sau khi xoá toàn bộ list là: ")
print(rs7)