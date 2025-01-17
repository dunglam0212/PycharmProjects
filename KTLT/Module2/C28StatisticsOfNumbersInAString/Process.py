def statistic_numbers(string):
    #string = “5;7;8;-2;8;11;13;9;10”
    numbers = string.split(';')
    #In các số trên những dòng riêng biệt:
    for n in numbers:
        print(n)

#Thống kê các số chẵn:
def statistic_even_numbers(string):
    # string = “5;7;8;-2;8;11;13;9;10”
    numbers = string.split(';')
    stat_even = 0
    for n in numbers:
        if int(n)%2==0:
            stat_even+=1
    return stat_even

#Thống kê các số âm
def statistic_negative_numbers(string):
    # string = “5;7;8;-2;8;11;13;9;10”
    numbers = string.split(';')
    neg_number = 0
    for n in numbers:
        if int(n)<0:
            neg_number+=1
    return neg_number

#Kiểm tra 1 số bất kỳ có phải là số nguyên tố hay không?
def check_prime_number(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    return False

#Thống kê các số nguyên tố
def statistic_prime_numbers(string):
    # string = “5;7;8;-2;8;11;13;9;10”
    numbers = string.split(';')
    prime_numbers = 0
    for n in numbers:
        rs = check_prime_number(int(n))
        if rs == True:
            prime_numbers+=1
    return prime_numbers

#Tính giá trị trung bình
def avg(string):
    # string = “5;7;8;-2;8;11;13;9;10”
    numbers = string.split(';')
    sum = 0
    for n in numbers:
        sum+=int(n)
    avg = sum/len(string)
    return avg
