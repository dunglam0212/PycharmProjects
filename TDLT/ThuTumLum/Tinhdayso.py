def tinh(n):
    s=0
    for i in range(1,n+1):
        s = s + 1/(i*(i+1))
        x = n/(n+1)
    if round(s,10) == round(x,10):
        return True
    else:
        return False

print(tinh(100))
