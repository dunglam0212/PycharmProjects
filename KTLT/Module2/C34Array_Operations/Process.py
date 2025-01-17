import array

from Module2.C28StatisticsOfNumbersInAString.Process import check_prime_number


#arr_int = [-96, -93, -82, -59, 29, 45, 48, 69, 70, 88]

#Đếm các số lẻ trong mảng:
def count_odd(arr_int):
    odd = 0
    list_odd = []
    for a in arr_int:
        if int(a)%2==0:
            pass
        else:
            odd+=1
            list_odd.append(a)
    return odd, list_odd

#Đếm các số chẵn trong mảng:
def count_even(arr_int):
    even = 0
    list_even = []
    for a in arr_int:
        if int(a)%2==0:
            even += 1
            list_even.append(a)
    return even, list_even

#Thống kê các SNT trong mảng:
def stat_prime_numbers(arr_int):
    list_prime_numbers = []
    for a in arr_int:
        rs = check_prime_number(int(a))
        if rs == True:
            list_prime_numbers.append(a)
    return list_prime_numbers

#Thống kê các số không phải là SNT trong mảng:
def stat_not_prime_numbers(arr_int):
    list_not_prime_numbers = []
    for a in arr_int:
        rs = check_prime_number(int(a))
        if rs == False:
            list_not_prime_numbers.append(a)
    return list_not_prime_numbers

#Mảng sau khi xoá các số chẵn:
def del_even_numbers(arr_int):
    #arr_int = [-96, -93, -82, -59, 29, 45, 48, 69, 70, 88]
    for a in arr_int[:]:  # Dùng arr_int[:] để tạo bản sao
        if int(a) % 2 == 0:
            arr_int.remove(a)
    return arr_int
