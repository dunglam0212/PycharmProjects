def check_positive_number():
    n = int(input('Nhập số tháng gửi: '))
    if n > 0:
        return n
    else:
        print('This is not a valid number! Please try again.')

def operate():
    flag = True
    while flag:
        p = float(input('Nhập vào số tiền gửi ban đầu: '))
        if p >0:
            while flag:
                N = check_positive_number()
                if N == 1:
                    k = 0.5
                    f = p * ((1 + k) ** N)
                    print(f'Số tiền nhận được sau {N} tháng là: {f}')
                    flag = False
                elif N == 6:
                    k = 0.6
                    f = p * ((1 + k) ** N)
                    print(f'Số tiền nhận được sau {N} tháng là: {f}')
                    flag = False
                else:
                    print('Vui lòng nhập lại số tháng gửi là 1 tháng hoặc 6 tháng!')
        else:
            print('Vui lòng nhập số tiền gửi ban đầu là một số dương')

operate()

def choice():
    a = True
    users_choice = input('Do you want to continue? Y/N: ')
    if users_choice.upper() == 'Y':
        operate()
    if users_choice.upper() == 'N':
        a = False
    else:
        print('Please enter Y to continue or N to stop!')
