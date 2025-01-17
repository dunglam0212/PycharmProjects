def GCD(a,b):
    if a<b:
        return GCD(b,a)
    x = a%b
    if x == 0:
        return b
    return GCD(a,x)
