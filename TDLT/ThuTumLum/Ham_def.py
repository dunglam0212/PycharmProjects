#hàm không có đối số
def chialaydu():
    a=3
    b=5
    P = a%b
    return P
result = chialaydu()
print('Kết quả của 3%5 =', result)
print('-'*30)

#Hàm có đối số và không trả về kết quả
def hello(name):
    print(f'Xin chào {name}!') #Đây không phải là kết quả trả về của hàm hello(name)
name = input('Xin hãy nhập tên của bạn: ')
result = hello(name)
#Khi gọi hàm hello(name) thì chương trình thực hiện dòng 3 và xuất ra màn hình
print('Kết quả của hàm có đối số và không trả về kết quả:', result)
#Vì là hàm không trả về kết quả nên khi chạy dòng 7 thì có kết quả là None
print('-'*30)

#Hàm có đối số và có trả về kết quả
def double(n):
    return n*2
result = double(3)
print('Kết quả của hàm có đối số và có trả về kết quả:',result)





