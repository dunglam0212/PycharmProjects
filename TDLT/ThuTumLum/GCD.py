#1. Hãy viết lại tìm ước số chung lớn nhất của 2 số A B
'''a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
while a!=b:
    if a > b:
        a = a-b
    else:
        b = b-a
print(f"Ước chung lớn nhất của 2 số {a} và {b} là:", a)'''
#Cách 1:
def gcd(a,b):
    while a!=b:
        if a>b:
            a = a - b
        else:
            b = b - a
    return a
'''
Cách 2:
#Quy luật: Sau mỗi bước tính thì độ lớn của 2 số a và b sẽ đảo ngược nhau.
VD: ban đầu a>b, sau khi a%b --> a<b
    ban đầu a<b, sau khi b%a --> a>b
def gcd(a,b): --> only in Python
    while b!=0: #Điểm dừng khi b=0
        a,b=b,a%b
    return a
    
def gcd(a,b):
    while b!=0: #Điểm dừng khi b=0
        c=b
        b=a%b
        a=c
    return a'''

def operate():
    x = int(input("Please enter a positive integer: "))
    y = int(input("Please enter another positive integer: "))
    if x<=0:
        x = int(input('Please enter a positive integer! '))
    elif y<=0:
        y = int(input('Please enter another positive integer! '))
    else:
        print(f'Greatest common divisor of {x} and {y} is: {gcd(x,y)}')

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



