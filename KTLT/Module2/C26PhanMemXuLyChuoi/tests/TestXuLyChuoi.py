from Module2.C26PhanMemXuLyChuoi.model.XuLyChuoi import *

chuoi = "TRần tHanH tHẢn"
chuoi1 = "tHadnfS FSD fgdf SJF"
chuoi2 = "232kjnjY sdT,?GVjbf453"
chuoi3 = "TRầ!?n12 tH45a.nH tHẢ,n"

rs = count_capital_character(chuoi3)
print(f"Số ký tự in hoa trong chuỗi '{chuoi3}' là: {rs}")

rs = print_uppercase(chuoi3)
print(f"Các ký tự in hoa trong chuỗi '{chuoi3}' là: {rs}")

rs = count_lowercase(chuoi3)
print(f"Số ký tự thường trong chuỗi '{chuoi3}' là: {rs}")

rs = print_lowercase(chuoi3)
print(f"Các ký tự thường trong chuỗi '{chuoi3}' là: {rs}")

rs = count_number(chuoi3)
print(f"Số chữ số trong chuỗi '{chuoi3}' là: {rs}")

rs = count_special_character(chuoi3)
print(f"Số ký tự đặc biệt trong chuỗi '{chuoi3}' là: {rs}")

rs = count_space(chuoi3)
print(f"Số khoảng trắng trong chuỗi '{chuoi3}' là: {rs}")

rs = count_vowels(chuoi3)
print(f"Số nguyên âm trong chuỗi '{chuoi3}' là: {rs}")

rs, list = count_consonants(chuoi3)
print(f"Số phụ âm trong chuỗi '{chuoi3}' là: {rs}")
print(f"Các phụ âm trong chuỗi'{chuoi3}' là: {list}")

list1 = count_a_word(chuoi3)
print(f"Số từ trong chuỗi '{chuoi3}' là: {list1}")