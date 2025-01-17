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