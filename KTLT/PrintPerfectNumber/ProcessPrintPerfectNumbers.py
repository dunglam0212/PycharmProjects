def print_perfect_numbers(n):
    if n>0:
        s = 0
        for i in range(1,n):
            if n%i == 0:
                s+=i
        if s==n:
            return True

def print_perfect_numbers_from_1_to_N(N):
    list = []
    for i in range(1,N+1):
        s = 0
        for j in range(1, (i//2)+1):
            if i%j  == 0:
                s += j
        if s == i:
            list.append(i)
    return list