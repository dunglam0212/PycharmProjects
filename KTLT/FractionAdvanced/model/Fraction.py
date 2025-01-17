#Tối giản, cộng, trừ, nhân, chia phân số

def parse_fraction(f):
    #f có dạng: a/b
    parts = f.split("/")
    if len(parts)>2:
        return False
    numerator = int(parts[0])
    denominator = int(parts[1])
    parts = [numerator, denominator]
    return parts

def simplify_fraction(f):
    # f có dạng: [a,b]
    a,b = f[0], f[1]
    m = a/b
    if m==0:
        return "0"
    elif m==1:
        return"1"
    elif m==2:
        return"2"
    elif m==3:
        return "3"
    elif m==4:
        return "4"
    elif m==5:
        return "5"
    elif m==6:
        return "6"
    elif m==7:
        return "7"
    elif m==8:
        return "8"
    elif m==9:
        return "9"
    else:
        numerator = a//gcd(a,b)
        denominator = b//gcd(a,b)
        #Phải lấy phần nguyên vì nếu để phép chia thông thường
        #thì sẽ trả về kết quả dưới dạng số thực
        #vd: thay vì là [5,2] --> [5.0,2.0]
        return [numerator,denominator]

def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

# Cách khác ngắn gọn hơn:
# def gcd(a,b):
#     while b!=0: #Điểm dừng khi b=0
#         a,b=b,a%b
#     return a

def add_fractions(f1,f2):
    #f1, f2 có dạng a/b:
    fraction1 = parse_fraction(f1)
    numerator1 = fraction1[0]
    denominator1 = fraction1[1]
    fraction2 = parse_fraction(f2)
    numerator2 = fraction2[0]
    denominator2 = fraction2[1]
    if denominator1 == 0 or denominator2 == 0:
        return False
    else:
        fraction_add = str(numerator1*denominator2+numerator2*denominator1) + "/" + str(denominator1*denominator2)
        parts = parse_fraction(fraction_add)
        fraction_add_simplify = simplify_fraction(parts)
        if len(fraction_add_simplify) == 1:
            return fraction_add_simplify
        else:
            fraction = str(fraction_add_simplify[0]) + "/" + str(fraction_add_simplify[1])
            return fraction

def substract_fractions(f1,f2):
    #f1, f2 có dạng a/b:
    fraction1 = parse_fraction(f1)
    numerator1 = fraction1[0]
    denominator1 = fraction1[1]
    fraction2 = parse_fraction(f2)
    numerator2 = fraction2[0]
    denominator2 = fraction2[1]
    if denominator1 == 0 or denominator2 == 0:
        return False
    else:
        fraction_substract = str(numerator1*denominator2-numerator2*denominator1) + "/" + str(denominator1*denominator2)
        parts = parse_fraction(fraction_substract)
        fraction_substract_simplify = simplify_fraction(parts)
        if len(fraction_substract_simplify) == 1:
            return fraction_substract_simplify
        else:
            fraction = str(fraction_substract_simplify[0]) + "/" + str(fraction_substract_simplify[1])
            return fraction

def multiple_fractions(f1,f2):
    #f1, f2 có dạng a/b:
    fraction1 = parse_fraction(f1)
    numerator1 = fraction1[0]
    denominator1 = fraction1[1]
    fraction2 = parse_fraction(f2)
    numerator2 = fraction2[0]
    denominator2 = fraction2[1]
    if denominator1 == 0 or denominator2 == 0:
        return False
    else:
        fraction_multiple = str(numerator1*numerator2) + "/" + str(denominator1*denominator2)
        parts = parse_fraction(fraction_multiple)
        fraction_multiple_simplify = simplify_fraction(parts)
        if len(fraction_multiple_simplify ) == 1:
            return fraction_multiple_simplify
        else:
            fraction = str(fraction_multiple_simplify[0]) + "/" + str(fraction_multiple_simplify[1])
            return fraction

def divide_fractions(f1,f2):
    #f1, f2 có dạng a/b:
    fraction1 = parse_fraction(f1)
    numerator1 = fraction1[0]
    denominator1 = fraction1[1]
    fraction2 = parse_fraction(f2)
    numerator2 = fraction2[0]
    denominator2 = fraction2[1]
    if denominator1 == 0 or denominator2 == 0 or numerator2 == 0:
        return False
    else:
        fraction_divide = str(numerator1*denominator2) + "/" + str(denominator1*numerator2)
        parts = parse_fraction(fraction_divide)
        fraction_divide_simplify = simplify_fraction(parts)
        if len(fraction_divide_simplify) == 1:
            return fraction_divide_simplify
        else:
            fraction = str(fraction_divide_simplify[0]) + "/" + str(fraction_divide_simplify[1])
            return fraction