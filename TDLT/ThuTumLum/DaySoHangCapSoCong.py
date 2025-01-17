def CSC(m,n,a,d):
    if a>n or a<m:
        print('a phai nam trong khoang tu m den n!')
    else:
        for i in range(m,n+1):
            x=a+d*(i-1)
            if m<x<=n:
                print(x)

m,n,a,d = eval(input('Nhap: '))
CSC(m,n,a,d)