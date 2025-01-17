def tinh(N):
    S=1
    i=1
    while (i<=N):
        if(i%3==0):
           S*=i
        i+=1
    return S
N=8
for i in range(1,10):
    if (i>N):
        print('==='+str(tinh(i)))

