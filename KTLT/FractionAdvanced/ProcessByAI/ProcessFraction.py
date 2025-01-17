from math import gcd


'''def input_fractions(n):
    """
    Nhập n phân số vào danh sách dưới dạng [a, b].
    """
    fractions = []
    for i in range(n):
        f = input("Nhập phân số dạng a/b:")
        parts = parse_fraction(f)
        a, b = parts[0], parts[1]
        fractions.append([a,b])
    return fractions'''

def parse_fraction(fraction_str):
    """
    Chia phân số từ dạng 'a/b' thành danh sách [a, b].
    """
    parts = fraction_str.split('/')
    if len(parts) != 2:
        return False #"Phân số phải có dạng 'a/b'
    numerator = int(parts[0])
    denominator = int(parts[1])
    if denominator == 0:
        return False #"Mẫu số không thể bằng 0
    return [numerator, denominator]

def simplify_fraction(fraction):
    #Rút gọn phân số:
    a, b = fraction
    common_divisor = gcd(a, b)
    return [a // common_divisor, b // common_divisor]

def output_fraction(fraction):
    a = fraction[0]
    b = fraction[1]
    f = f"{a}/{b}"
    return f







