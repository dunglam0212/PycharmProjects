def H10T0H16(n):
    if n>0:
        sd = n%16
        n = n//16
        if sd == 13:
            sd = 'D'
        elif sd == 11:
            sd = 'B'
        else:
            pass
        H10T0H16(n)
        print(sd, end='')

H10T0H16(317547)