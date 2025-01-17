from Module2.C33PhanMemTuongTacMang.Process import return_random_array, sum_array, find_smallest_item, increase_2_digit, \
    count_odds, sum_odds, sort_asc, sort_dsec

array = return_random_array()
print("Mảng gồm 10 phần tử ngẫu nhiên là: ")
print(array)

sum_array = sum_array(array)
print(f"Tổng của mảng trên là: {sum_array}")

small = find_smallest_item(array)
print(f"Phần tử nhỏ nhất trong mảng là: {small}")

# increase_2 = increase_2_digit(array)
# print(f"Mảng sau khi tăng mỗi phần tử thêm 2 đơn vị là: {array}")

count_odd_numbers = count_odds(array)
print(f"Số phần tử lẻ trong mảng trên là: {count_odd_numbers}")

sum_odd = sum_odds(array)
print(f"Tổng các phần tử lẻ trong mảng trên là: {sum_odd}")

asc_arr = sort_asc(array)
print(f'Mảng sau khi sắp xếp tăng dần là: {asc_arr}')

dsec_arr = sort_dsec(array)
print(f'Mảng sau khi sắp xếp tăng dần là: {dsec_arr}')