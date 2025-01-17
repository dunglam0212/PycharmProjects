from CalculateWithFractions.process.Fraction import parse_fraction
from FractionAdvanced.model.Fractions import quick_sort_fractions, list_fractions, sort_ascending, sort_descending

list = [1,5,8,4,8]
print(len(list)-1)

f_find = "6/8"
f = parse_fraction(f_find)
rs = quick_sort_fractions(f,list_fractions,0,len(list_fractions))
if rs == -1:
    print(f"Không tìm thấy phân số {f_find}")
else:
    print(f"Đã tìm thấy phân số {f_find}")

list_fractions_asc = sort_ascending(list_fractions)
print(list_fractions_asc)

list_fractions_dsec = sort_descending(list_fractions)
print(list_fractions_dsec)