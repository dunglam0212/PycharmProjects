def ve_hinh_vuong(h):
    for i in range(h):
        for j in range(h):
            print('*', end =' ')
        print('')
#Mặc định là chiều dài là trục hoành, chiều rộng là trục tung
def ve_hinh_cnhat(cd,cr):
    for i in range(cr):
        for j in range(cd):
            print('*', end=' ')
        print('')

def ve_hinh_tgiacv(h):
    for i in range(h):
        for j in range(i+1):
            print('*', end=' ')
        print('')

def ve_hbh(h):
    for i in range(h):
        for j in range(h-i):
            print(' ', end=' ')
        for k in range(h+1):
            print('*', end=' ')
        print('')

def ve_tgiac_can(h):
    for i in range(h):
        for j in range(h-i):
            print(' ', end='')
        for k in range(i+1):
            print('*', end=' ')
        print('')

def ve_hinh_thoi(h):
    for i in range(h+1):
        for j in range(h-i):
            print(' ', end='')
        for k in range(i+1):
            print('*', end=' ')
        print('')
    for i in range(h+1):
        for j in range(i+1):
            print(' ', end='')
        for k in range(h-i):
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

def vetg_rong(h):
    for i in range(h):
        for j in range(h):
            if j==0 or i==h-1 or i==j:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def vetg_rong_ngc(h):
    for i in range(h):
        for j in range(h-i):
            if i==0 or j==0 or (i+j)==h-1:
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
vehinh4(3)