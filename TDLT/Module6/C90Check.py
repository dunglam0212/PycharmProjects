a = 0
i = 0
while a<100:
    b=0
    while b<40:
        if (a+b)%2==0:
            print('*', end='')
            i+=1
        b+=1
    print()
    a+=1
print(i)

