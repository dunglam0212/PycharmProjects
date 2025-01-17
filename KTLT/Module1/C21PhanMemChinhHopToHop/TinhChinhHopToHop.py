#Công thức tính chỉnh hợp và tổ hợp chập k của n:
#Ak,n = n!/(n-k)!
#Ck, n = n!/(k!*(n-k)!)

def giai_thua(n):
    gt = 1
    for i in range(1,n+1):
        gt = gt*i
    return gt

def chinh_hop(k,n):
    return giai_thua(n)/giai_thua(n-k)

def to_hop(k,n):
    return (giai_thua(n)/(giai_thua(k)*giai_thua(n-k)))

