from random import randint

def create_list():
    list = []
    for i in range(10):
        x = randint(-100, 101)
        list.append(x)
    return list

def append_list(p, list):
    list.append(p)
    return list

def check_frequency(k,list):
    f = 0
    for l in list:
        if l == k:
            f+=1
    return f

def check_perfect_number(n):
    s = 1
    for i in range(2,(n//2)+1):
        if n%i ==0:
            s+=i
    if s == n:
        return True

def sum_perfect_number(list):
    s=0
    for l in list:
        check = check_perfect_number(l)
        if check == True:
            s+=l
    return s

def sort_asc(list):
    pass