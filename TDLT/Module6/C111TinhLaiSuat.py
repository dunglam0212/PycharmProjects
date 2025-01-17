def tgtk(A,N,r):
    n = N*4
    for i in range(1,n+1):
        A = A*(1+3*r)
    return round(A,-3)
print(tgtk(10000000,2,0.05))

A = 123456789.99
print(round(A,-3)) #làm tròn đến hàng nghìn
print(round(A)) #hàng chục nghìn
