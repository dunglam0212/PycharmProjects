# Cần thực hiện các thao tác với chuỗi:
# 1. Bao nhiêu chữ IN HOA
# 2. Bao nhiêu chữ in thường
# 3. Bao nhiêu chữ là chữ số
# 4. Bao nhiêu chữ là ký tự đặc biệt
# 5. Bao nhiêu chữ là khoảng trắng
# 6. Bao nhiêu chữ là Nguyên Âm
# 7. Bao nhiêu chữ là Phụ âm
# 8. Bao nhiêu từ

#Danh sách các ký tự in hoa (có tính dấu thanh) trong tiếng Việt
list_uppercase = ['A', 'Ă', 'Â', 'B', 'C', 'D', 'Đ', 'E', 'Ê', 'G', 'H', 'I', 'K',
    'L', 'M', 'N', 'O', 'Ô', 'Ơ', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ư',
    'V', 'X', 'Y', 'Á', 'À', 'Ả', 'Ã', 'Ạ',
    'Ắ', 'Ằ', 'Ẳ', 'Ẵ', 'Ặ',
    'Ấ', 'Ầ', 'Ẩ', 'Ẫ', 'Ậ',
    'É', 'È', 'Ẻ', 'Ẽ', 'Ẹ',
    'Ế', 'Ề', 'Ể', 'Ễ', 'Ệ',
    'Í', 'Ì', 'Ỉ', 'Ĩ', 'Ị',
    'Ó', 'Ò', 'Ỏ', 'Õ', 'Ọ',
    'Ố', 'Ồ', 'Ổ', 'Ỗ', 'Ộ',
    'Ớ', 'Ờ', 'Ở', 'Ỡ', 'Ợ',
    'Ú', 'Ù', 'Ủ', 'Ũ', 'Ụ',
    'Ứ', 'Ừ', 'Ử', 'Ữ', 'Ự',
    'Ý', 'Ỳ', 'Ỷ', 'Ỹ', 'Ỵ']

list_lowercase = ['a', 'ă', 'â', 'b', 'c', 'd', 'đ', 'e', 'ê', 'g', 'h', 'i', 'k',
    'l', 'm', 'n', 'o', 'ô', 'ơ', 'p', 'q', 'r', 's', 't', 'u', 'ư',
    'v', 'x', 'y','á', 'à', 'ả', 'ã', 'ạ',
    'ắ', 'ằ', 'ẳ', 'ẵ', 'ặ',
    'ấ', 'ầ', 'ẩ', 'ẫ', 'ậ',
    'é', 'è', 'ẻ', 'ẽ', 'ẹ',
    'ế', 'ề', 'ể', 'ễ', 'ệ',
    'í', 'ì', 'ỉ', 'ĩ', 'ị',
    'ó', 'ò', 'ỏ', 'õ', 'ọ',
    'ố', 'ồ', 'ổ', 'ỗ', 'ộ',
    'ớ', 'ờ', 'ở', 'ỡ', 'ợ',
    'ú', 'ù', 'ủ', 'ũ', 'ụ',
    'ứ', 'ừ', 'ử', 'ữ', 'ự',
    'ý', 'ỳ', 'ỷ', 'ỹ', 'ỵ']

list_number = ['0','1','2','3','4','5','6','7','8','9']

#Danh sách phụ âm in hoa:
consonants_uppercase = [
    'B', 'C', 'D', 'Đ', 'G', 'H', 'K', 'L', 'M', 'N',
    'P', 'Q', 'R', 'S', 'T', 'V', 'X']

#Danh sách phụ âm viết thường:
consonants_lowercase = [
    'b', 'c', 'd', 'đ', 'g', 'h', 'k', 'l', 'm', 'n',
    'p', 'q', 'r', 's', 't', 'v', 'x']

#1. Đếm số KT hoa
def count_capital_character(string):
    count = 0
    for i in range(len(string)):
        if string[i] in list_uppercase:
            count+=1
    return count

#1.1. In chữ hoa
def print_uppercase(string):
    list = []
    for i in range(len(string)):
        if string[i] in list_uppercase:
            list.append(string[i])
    return list

#2. Đếm số KT thường:
def count_lowercase(string):
    count = 0
    for i in range(len(string)):
        if string[i] in list_lowercase:
            count+=1
    return count

#2.1. In chữ thường
def print_lowercase(string):
    list = []
    for i in range(len(string)):
        if string[i] in list_lowercase:
            list.append(string[i])
    return list

#3. Đếm số chữ số:
def count_number(string):
    count = 0
    for i in range(len(string)):
        if string[i] in list_number:
            count+=1
    return count

#4. Đếm số ký tự đặc biệt
def count_special_character(string):
    count = 0
    string = string.replace(" ","")
    for i in range(len(string)):
        if ((string[i] not in list_number)
                and (string[i] not in list_uppercase)
                and (string[i] not in list_lowercase)):
            count+=1
    return count

#5. Đếm số khoảng trắng
def count_space(string):
    count = 0
    for i in range(len(string)):
        if string[i] == " ":
            count += 1
    return count

#6. Đếm số nguyên âm (kh phân biệt in hoa, viết thường)
def count_vowels(string):
    list = []
    string = string.replace(" ", "")
    for i in range(len(string)):
        if ((string[i] in list_uppercase
                     or string[i] in list_lowercase)
                and (string[i] not in consonants_lowercase)
                and (string[i] not in consonants_uppercase)):
            list.append(string[i])
    return list

#7. Đếm số phụ âm (kh phân biệt in hoa, viết thường)
def count_consonants(string):
    list = []
    string = string.replace(" ", "")
    for i in range(len(string)):
        if ((string[i] in list_uppercase
              or string[i] in list_lowercase)
            and (string[i] in consonants_lowercase
              or string[i] in consonants_uppercase)):
            list.append(string[i])
    return list

#Đếm số từ trong chuỗi (coi như 1 từ là kẹp giữa 2 dấu cách, kh xét nghĩa của từ)
def count_a_word(string):
    list = string.split(" ")
    return list