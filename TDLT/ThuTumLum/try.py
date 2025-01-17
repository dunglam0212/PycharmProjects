'''print("Hello")
x=3
y=5
print("Ket qua cua x cong y la",x+y)
print("Ket qua la " + str(x))

prompt = "Tell me something cool: "
prompt += "\nEnter 'quit' to end the program"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)'''

def gcd(a,b):
    while a!=b:
        if a>b:
            a = a - b
        else:
            b = b - a
    return a

def check_positive_number():
    while True:
        try:
            number = int(input('Please enter a positive number: '))
            if number > 0:
                return number
            else:
                print('This is not a positive number! Please try again.')
        except ValueError:
            print('This is not a valid number. Please try again.')

def operate():
    x = check_positive_number()
    y = check_positive_number()
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

