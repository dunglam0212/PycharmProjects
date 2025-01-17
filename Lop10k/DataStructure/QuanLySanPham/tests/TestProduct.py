from DataStructure.QuanLySanPham.models.Product import Product

p1 = Product('p1', 'Thuốc trị hôi nách',15,30 ) #nhớ (): cú pháp
#xuất đối tượng p1 ra màn hình
print('Thông tin của p1: ')
print(p1) #lúc này hàm __str__ tự động được gọi
p1.name = 'Thuốc trị lang beng'
print('Tên p1 sau khi sửa tên: ',p1)
p1.price = 45
print('Sản phẩm sau khi sửa giá: ')
print(p1)

p1.id='P113'
p1.name='Dep Lào'
p1.quantity=2
p1.price=100
print(p1)

p2=Product('P114', 'Dép Tổ ong', 30,140)
print('Dữ liệu của p2:',p2)

p3=Product('P115', 'Nón lá')
print('Dữ liệu cuả p3: ',p3)

#on lại Alias
p4=p3
#--> Lúc này ổ nhớ mà p3 đang quản lý, có thêm p4 quản lý
#--> alias: p4 đổi gtri trong ổ nhớ sẽ làm p3 đổi, và ngc lại
p4.quantity=999
print('Dữ liệu của p3:')
print(p3)
p3.quantity=500
print('Dữ liệu cua p4:')
print(p4)

a=Product(name='Dép lào')
b=a
c=Product(name='Thuốc lào')
b=c
b.name = 'Gió lào'
#hỏi: a.name bằng bao nhiêu? --> Dép Lào
print('Tên của a: ',a.name)


