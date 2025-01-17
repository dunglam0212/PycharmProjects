from DataStructure.S1Factorial.Factorial import *
from DataStructure.S1Factorial.Fibonacci import fibo, list_fib
from DataStructure.S1Factorial.GCD import GCD
from DataStructure.S1Factorial.HanoiTower import hanoi_tower

f5 = factorial_non_recursive(5)
print(f'5! = {f5}')

for i in range(0,11):
    fi = factorial_non_recursive(i)
    print(f'{i}! = {fi}')

print('-------Recursive-------')
f5r = factorial_recursive(5)
print(f'{5}! = {f5r}')

print('-------Test Tổ hợp & Chỉnh hợp-------')
n = 5
k = 2
print(f'A({n},{k}) = {A(n,k)}')
print(f'C({n},{k}) = {C(n,k)}')

print('------------Test tính ước chung lớn nhất-------------------')
print(f'Ước chung lớn nhất của 3 và 7 là: {GCD(3,7)}')
print(f'Ước chung lớn nhất của 145 và 745 là: {GCD(145,745)}')

print('--------Test Fibonacci------------')
print(f'Số hạng thứ 5 trong dãy Fibonacci mà bạn cần tìm là: {fibo(7)}')
print("Danh sách các phần tử của dãy Fibonacci từ 1 đến 7 là: ")
list_fib(7)

print('-----------Test Hanoi_Tower--------')
n = 3
hanoi_tower(n,"A","B","C")
