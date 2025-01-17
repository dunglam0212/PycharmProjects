from math import sqrt

def tinh(n):
    s = sqrt(2)
    for i in range(2,n+1):
        s = sqrt(2+s)
    return s
print(tinh(4))