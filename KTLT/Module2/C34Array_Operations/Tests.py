from Module2.C34Array_Operations.Process import *

arr_int = [-96, -93, -82, -59, 29, 45, 48, 69, 17, 70, 88]
for a in arr_int:
    print(a)

odd, list_odd = count_odd(arr_int)
print(f'Các số lẻ trong mảng trên là: {list_odd}')
print(f"Trên mảng trên có {odd} số lẻ")

even, list_even = count_even(arr_int)
print(f'Các số chẵn trong mảng trên là: {list_even}')
print(f"Trên mảng trên có {even} số chẵn")

prime = stat_prime_numbers(arr_int)
print(f"Các SNT trong mảng trên là: {prime}")

prime1 = stat_not_prime_numbers(arr_int)
print(f"Các số không là SNT trong mảng trên là: {prime1}")

rs = del_even_numbers(arr_int)
print(f"Mảng sau khi xoá các số chẵn là: {rs}")