from CalculateWithFractions.process.Fraction import gcd, simplify_fraction, add_fractions, substract_fractions
from FractionAdvanced.ProcessByAI.ProcessFraction import parse_fraction

n = input('enter a fraction with type "a/b":  ')
print(parse_fraction(n))

print(gcd(20,8))

print(simplify_fraction([20,8]))

rs = add_fractions("3/4", "5/6")
if rs == False:
    print('Phân số không hợp lệ! Vui lòng nhập mẫu số khác 0')
else:
    print(rs)

rs = substract_fractions("3/4", "3/4")
if rs == False:
    print('Phân số không hợp lệ! Vui lòng nhập mẫu số khác 0')
else:
    print(rs)