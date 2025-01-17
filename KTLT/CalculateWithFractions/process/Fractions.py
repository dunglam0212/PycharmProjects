from CalculateWithFractions.process.Fraction import parse_fraction

#Giả sử mình có 1 danh sách ng dùng nhập vào 5 phân số có dạng [a,b]
list_fractions = [[1, 5], [34, 67], [567, 89], [6, 8], [6, 3]]

#Cần làm cách chức năng: thêm, sửa, xoá, xem(tìm kiếm, phân loại, sắp xếp)

def find_fraction_in_list_fractions(f):
    #Giả sử f cần tìm có dạng 'a/b'
    fraction = parse_fraction(f)
    for f in list_fractions:
        if f == fraction:
            return True

def add_fraction_to_list_fractions(f):
    # Giả sử f cần thêm có dạng 'a/b'
    fraction = parse_fraction(f)
    list_fractions.append(fraction)
    return list_fractions

def remove_fraction_from_list_fractions(f):
    # Giả sử f cần xoá có dạng 'a/b'
    find = find_fraction_in_list_fractions(f)
    fraction = parse_fraction(f)
    if find == True:
        list_fractions.remove(fraction)
        return True
def sort_fraction(min, max):
    list_sort = []
    #Giả sử min, max có dạng 'a/b'
    parts_min = parse_fraction(min)
    parts_max = parse_fraction(max)
    min_float = parts_min[0]/parts_min[1]
    max_float = parts_max[0]/parts_max[1]
    list_fractions_float = []
    for f in list_fractions:
        fraction = f[0] / f[1]
        list_fractions_float.append(fraction)
    for f in list_fractions_float:
        if f >= min_float and f <= max_float:
            index = list_fractions_float.index(f)
            fraction = list_fractions[index]
            list_sort.append(fraction)
    return list_sort

def sort_ascending(list):
    list_sort = []
    list_fractions_float = []
    for f in list_fractions:
        fraction = f[0] / f[1]
        list_fractions_float.append(fraction)
    for i in range(len(list_fractions_float)):
        for j in range(i+1, len(list_fractions_float)):
            fi = list_fractions_float[i]
            fj = list_fractions_float[j]
            if fi > fj:
                list_fractions_float[j] = fi
                list_fractions_float[i] = fj
    for f in list_fractions_float:
        index = list_fractions_float.index(f)
        fraction = list_fractions[index]
        list_sort.append(fraction)
    return list_sort

def sort_descending(list):
    list_sort = []
    list_fractions_float = []
    for f in list_fractions:
        fraction = f[0] / f[1]
        list_fractions_float.append(fraction)
    for i in range(len(list_fractions_float)):
        for j in range(i + 1, len(list_fractions_float)):
            fi = list_fractions_float[i]
            fj = list_fractions_float[j]
            if fi < fj:
                list_fractions_float[j] = fi
                list_fractions_float[i] = fj
    for f in list_fractions_float:
        index = list_fractions_float.index(f)
        fraction = list_fractions[index]
        list_sort.append(fraction)
    return list_sort