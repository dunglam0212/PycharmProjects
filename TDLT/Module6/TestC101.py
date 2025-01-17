import time


def vehinh1(h):
    for i in range(h):
        for j in range(h):
            print(' ', end=' ')
        for k in range(i+1):
            print('*', end=' ')
        print('')
    for i in range(h*2+1):
        print('*', end=' ')
    print('')
    for i in range(h+1):
        for t in range(h-i):
            print('*', end=' ')
        print('')

def vehinh2(h):
    for i in range(h):
        for j in range(h):
            print(' ', end=' ')
        for k in range(h):
            if k==0 or i==k:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    for i in range(h*2+1):
        print('*', end=' ')
    print()
    for i in range(h):
        for j in range(h-i):
            if j==0 or (i+j)==h-1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def vehinh3(h):
    for i in range(h):
        for j in range(h):
            print(' ', end=' ')
        for k in range(h-i+1):
            print('*', end=' ')
        print()
    for i in range(h+1):
        for j in range(h-i):
            print(' ', end=' ')
        for k in range(i+1):
            print('*', end=' ')
        print()

def vehinh4(h):
    for i in range(h):
        for j in range(h):
            print(' ', end=' ')
        for k in range(h+1):
            if i==0 or k==0 or (i+k)==h:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    for i in range(h+1):
        for j in range(h+1):
            if i==h or j==h or (i+j)==h:
                print('*', end=' ')
            else:
                print(' ',end =' ')
        print()

vehinh1(3)
time.sleep(5)
vehinh2(3)