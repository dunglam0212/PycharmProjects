#Ý tưởng: 357 = 3*100 + 5*10 + 7
def dao_nguoc(x1,x2,x3):
    print(f'Số sau khi đảo ngược là: {x3}{x2}{x1}')

flag = True
while flag:
    try:
        x = int(input('Nhập vào một số có 3 chữ số: '))
        x1 = x // 100  #Lấy chữ số hàng trăm
        x2 = (x % 100) // 10  #Lấy chữ số hàng chục
        x3 = (x % 100) % 10  #Lấy chữ số hàng đơn vị
        dao_nguoc(x1,x2,x3)
        flag = False
    except:
        print('Giá trị không hợp lệ!')

#Vậy nếu có 4 chữ số thì sao? --> 3579
'''--> Thấy được quy luật: với x là số ban đầu, n là số chữ số nhập vào
 Chữ số đầu (từ trái sang phải) = x // (10^(n-1))
 Chữ số thứ 2 (từ trái sang) = (x % (10^(n-1))) // (10^(n-2))
 Chữ số thứ 3 (từ trái sang) = (x % (10^(n-1))) % (10^(n-2))
 Chữ số thứ 4 = '''







