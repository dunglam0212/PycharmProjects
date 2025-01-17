for val in "Lâm Thùy Dung":
    if val == "u":
        break #Break ở đây sẽ tạm dừng thực hiện lệnh val khi thỏa điều kiện if
    print(val)
print("Done")

for val in "Lâm Thùy Dung":
    if val == "u":
        continue #Lệnh continue thì bỏ qua đk thỏa, xong vẫn tiếp tục chạy lệnh if
    print(val)
print("Done")

a = 50
b = 100

if b < a:
    print("b không lớn hơn a")
    pass
else:
    print("b lớn hơn a")
"""Dòng code trên kh in ra "b kh lơớn hơn a" do lệnh pass đã bỏ qua việc xử lý
    nếu như b<a"""


