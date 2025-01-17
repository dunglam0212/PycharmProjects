def H10ToH16(n):
    if n>0:
        sd = n% 16
        n = n//16
        H10ToH16(n)
        if sd == 2:
            sd = 'A'
        elif sd == 3:
            sd='B'
        elif sd == 13:
            sd = 'D'
        elif sd == 11:
            sd='B'
        elif sd == 0:
            sd = '8'
        print(sd, end='')

H10ToH16(317547)