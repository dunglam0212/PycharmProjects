from random import randint

def create_list(list):
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
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i]>list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

def sort_desc(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i]<list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

def remove_an_element(itm,list):
    for l in list[:]:
        if l==itm:
            list.remove(itm)
            del itm
            return True

def remove_neg_numbers(list):
    for l in list[:]:
        if l<0:
            list.remove(l)
            del l
    return list

def remove_all(list):
    for l in list[:]:
        list.remove(l)
        del l
    return list
