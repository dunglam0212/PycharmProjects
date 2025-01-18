from random import randint


def sort_asc(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i]>list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

def insert_item(itm, list):
    list.append(itm)
    return sort_asc(list)

def create_list():
    list = []
    for i in range(3):
        x = randint(-100,101)
        list.append(x)
    return list


