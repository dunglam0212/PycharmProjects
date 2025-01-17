import array as arr
from random import randint

#1. Xuất 1 mảng ngẫu nhiên gồm 10 số nguyên
def return_random_array():
    arr_int = None
    x = [randint(-100, 100) for a in range(10)]
    arr_int = arr.array("i",x)
    return arr_int

#2.Tính tổng giá trị mảng
def sum_array(array):
    sum=0
    for a in array:
        sum+=a
    return sum

#3. Tìm phần tử nhỏ nhất:
def find_smallest_item(array):
    a_smallest = array[0]
    for a in array:
        if a<a_smallest:
            a_smallest = a
    return a_smallest

#4.Tăng mỗi phần tử trong mảng lên 2 đơn vị
def increase_2_digit(array):
    for i in range(len(array)):
        array[i] = array[i] + 2
    return array

#5. Đếm số phần tử lẻ:
def count_odds(array):
    count = 0
    for a in array:
        if a%2!=0:
            count+=1
    return count

#6. Tính tổng giá trị phần tử lẻ:
def sum_odds(array):
    sum = 0
    for a in array:
        if a%2!=0:
            sum+=a
    return sum

#7. Sắp xếp mảng tăng dần:
def sort_asc(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

#8. Sắp xếp mảng giảm dần:
def sort_dsec(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array