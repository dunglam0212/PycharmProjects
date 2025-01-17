def vehinh1(h):
    for i in range(h):
        for j in range(h):
            if i==0 or j==0 or i==h-1 or j==h-1:
                print('*', end='  ')
            else:
                print(' ', end='  ')
        print()
vehinh1(4)

def vehinh2(h):
    for i in range(h):
        for j in range(h-i):
            print(' ', end='  ')
        for k in range(i+1):
            print('*', end='  ')
        print()
vehinh2(4)

def vehinh3(h):
    for i in range(h):
        for j in range(h):
            if j==0 or i==j:
                print('*', end='  ')
            else:
                print(' ', end='  ')
        print()
    for i in range(h*2+1):
        print('*', end='  ')
    print()
    for i in range(h):
        for j in range(h+1):
            print(' ', end='  ')
        for k in range(h):
            if k==h-1 or i==k:
                print('*', end='  ')
            else:
                print(' ', end='  ')
        print()
vehinh3(3)