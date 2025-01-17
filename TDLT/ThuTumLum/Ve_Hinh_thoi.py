#Vẽ hình thoi bằng *
def diamond(height):
    # In nửa trên hình thoi
    for i in range(height):
        #In khoảng trắng
        for j in range(height-i-1):
            print(' ', end='')
        #In dấu *
        for k in range(i+1):
            print('*', end=' ')
        print('')
    # In nửa dưới hình thoi
    for i in range(height):
        # In khoảng trắng
        for j in range(i + 1):
            print(' ', end='')
        # In dấu *
        for k in range(height - i - 1):
            print('*', end=' ')
        print('')

def check_positive_integer():
    while True:
        try:
            num = int(input('Please enter the size of the diamond (a positive integer): '))
            if num > 0:
                return num
            else:
                print('This is not a positive integer! Please try again.')
        except ValueError:
            print('That is not a valid number! Please enter again.')

def operate():
    h = check_positive_integer()
    diamond(h)

operate()
flag = True
while flag:
    users_choice = input('Do you want to continue? Y/N: ')
    if users_choice.upper() == 'Y':
        operate()
    if users_choice.upper() == 'N':
        flag = False
    else:
        print("Please enter 'Y' to continue or 'N' to stop!")