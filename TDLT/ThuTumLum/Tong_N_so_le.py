#Tính tổng N số lẻ đầu tiên
#Cách 1: Bình thường
'''N = int(input('Enter a positive integer: '))
s = 0
for i in range(1, 2*N, 2):
    s = s + i
print(f'Tổng của {N} số lẻ đầu tiên là: {s}')'''

#Cách 2: Dùng def
def check_positive_integer():
    while True:
        try:
            num = int(input('Enter a positive integer: '))
            if num > 0:
                return num
            else:
                print('This is not a positive integer! Please try again.')
        except ValueError:
            print('That is not a valid number! Please enter again.')

def sum_odd(n1):
    s = 0
    for i in range(1, 2*n1, 2):
        s = s + i
    return s

def operate():
    n2 = check_positive_integer()
    print(f'Tổng {n2} số lẻ đầu tiên là: {sum_odd(n2)}')

operate()

flag = True

while flag:
    users_choice = input('Do you want to continue? Y/N: ')
    if users_choice.upper() == 'Y':
        operate()
    elif users_choice.upper() == 'N':
        print('The program has ended!')
        flag = False
    else:
        print('Please enter Y to continue or N to stop!')