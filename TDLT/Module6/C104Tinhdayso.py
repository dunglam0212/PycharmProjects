def giaithua(n):
    gt = 1
    for i in range(n,0,-1):
        gt = gt*i
    return gt

def tinh(x,n):
    s=0
    for i in range(1,n+1):
        s = s + (x**i)/giaithua(i)
    return s
print(tinh(3,4))




