def check_perfect_num(n):
    s=0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            s+=i
    if s==n:
        return True
    else:
        return False
print(check_perfect_num(6))

def check_abundant_num(n):
    s=0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            s+=i
    if s>n:
        return True
    else:
        return False
print(check_abundant_num(12))
