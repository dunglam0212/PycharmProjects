from FractionAdvanced.ProcessByAI.ProcessFraction import simplify_fraction


def add_fractions(f1, f2):
    """
    Cộng hai phân số.
    """
    numerator = f1[0] * f2[1] + f2[0] * f1[1]
    denominator = f1[1] * f2[1]
    return simplify_fraction([numerator, denominator])

def subtract_fractions(f1, f2):
    """
    Trừ hai phân số.
    """
    numerator = f1[0] * f2[1] - f2[0] * f1[1]
    denominator = f1[1] * f2[1]
    return simplify_fraction([numerator, denominator])

def multiply_fractions(f1, f2):
    """
    Nhân hai phân số.
    """
    numerator = f1[0] * f2[0]
    denominator = f1[1] * f2[1]
    return simplify_fraction([numerator, denominator])

def divide_fractions(f1, f2):
    """
    Chia hai phân số.
    """
    numerator = f1[0] * f2[1]
    denominator = f1[1] * f2[0]
    return simplify_fraction([numerator, denominator])

def add_fraction_to_list(fractions, fraction):
    """
    Thêm phân số vào danh sách.
    """
    fractions.append(simplify_fraction(fraction))

def update_fraction_in_list(fractions, index, fraction):
    """
    Sửa phân số tại vị trí index trong danh sách.
    """
    if 0 <= index < len(fractions):
        fractions[index] = simplify_fraction(fraction)
    else:
        raise IndexError("Index không hợp lệ.")

def remove_fraction_from_list(fractions, index):
    """
    Xóa phân số tại vị trí index trong danh sách.
    """
    if 0 <= index < len(fractions):
        del fractions[index]
    else:
        raise IndexError("Index không hợp lệ.")

def find_fraction(fractions, fraction):
    """
    Tìm kiếm phân số trong danh sách.
    """
    fraction = simplify_fraction(fraction)
    for i, f in enumerate(fractions):
        if f == fraction:
            return i
    return -1

def sort_fractions(fractions):
    """
    Sắp xếp danh sách phân số theo giá trị tăng dần.
    """
    return sorted(fractions, key=lambda x: x[0] / x[1])

