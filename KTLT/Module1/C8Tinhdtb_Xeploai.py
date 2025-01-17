def average_score(math, physic, chemistry):
    aver_score = (math+physic+chemistry)/3
    if (aver_score<5):
        sort = 'Weak'
    elif (aver_score<7):
        sort = 'Ordinary'
    elif (aver_score<8):
        sort = 'Good'
    elif (aver_score<9):
        sort = 'Very Good'
    else:
        sort = 'Excellent'
    return aver_score, sort

def isFloat(n):
    try:
        n = float(n)
        if (0.0 <= n <= 10.0):
            return True
    except:
        return False

def main():
    flag = True
    math = input('Enter your math score: ')
    rs_m = isFloat(math)
    while rs_m == True:
        physic = input('Enter your physic score: ')
        rs_p = isFloat(physic)
        while rs_p == True:
            chemistry = input('Enter your chemistry score: ')
            rs_c = isFloat(chemistry)
            while rs_c == True:
                aver_score, sort = average_score(float(math), float(physic), float(chemistry))
                print(f'Your average score: {aver_score}')
                print(f'Your academic ranking: {sort}')
                ask()
                return
            print('Valid Error! Please enter your chemistry score again!')
        print('Valid Error! Please enter your physic score again!')
    print('Valid Error! Please enter your math score again!')
    main()

def ask():
    flag = True
    while flag:
        q = input('Do you want to continue? Y/N')
        if q.lower() == 'y':
            main()
            flag = False
        elif q.lower() == 'n':
            print('See you again!')
            return
        else:
            print('Valid error! Please choose Y or N!')

main()





