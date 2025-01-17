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

def sort_fraction(list, min, max):
    list_sort = []
    #Giả sử min, max có dạng 'a/b'
    parts_min = parse_fraction(min)
    parts_max = parse_fraction(max)
    min_float = parts_min[0]/parts_min[1]
    max_float = parts_max[0]/parts_max[1]
    list_fractions_float = []
    for f in list:
        fraction = f[0] / f[1]
        list_fractions_float.append(fraction)
    for f in list_fractions_float:
        if f >= min_float and f <= max_float:
            index = list_fractions_float.index(f)
            fraction = list[index]
            list_sort.append(fraction)
    return list_sort

def quick_sort_fractions(f, list, left, right):
    # f có dạng: [a,b]
    # left = 0
    # right = len(list_fractions)
    list_fractions_asc = sort_ascending(list)
    mid_index = (left+right)//2
    fraction1 = list_fractions_asc[mid_index]
    mid_item = fraction1[0]/fraction1[1]
    fraction = f[0]/f[1]
    if (left - right)<=1:
        if mid_item == fraction:
            return fraction
        else:
            return -1
    if mid_item < fraction:
        left = mid_index
        quick_sort_fractions(f,list, left, right)
    elif mid_item > fraction:
        right = mid_index
        quick_sort_fractions(f,list, left, right)


def sort_ascending(list):
    list_fractions_float = []
    for f in list:
        fraction = f[0] / f[1]
        list_fractions_float.append(fraction)
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list_fractions_float[i] > list_fractions_float[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

                temp1 = list_fractions_float[i]
                list_fractions_float[i] = list_fractions_float[j]
                list_fractions_float[j] = temp1
    return list

def sort_descending(list):
    list_fractions_float = []
    for f in list:
        fraction = f[0] / f[1]
        list_fractions_float.append(fraction)
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list_fractions_float[i] < list_fractions_float[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

                temp1 = list_fractions_float[i]
                list_fractions_float[i] = list_fractions_float[j]
                list_fractions_float[j] = temp1
    return list