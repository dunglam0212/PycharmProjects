from DataStructure.QuanLySanPham2.models.Product import Product

p1 = Product()
print('Thông tin của p1: ')
print(p1)

p1.id='P113'
p1.name='Dép Lào'
p1.quantity = 2
p1.price=100
print(p1)

p2=Product('P114', 'Dép tổ ong', 30,150)
print('Dữ liệu của p2:')
print(p2)

p3=Product('P115')
print('Dữ liệu của p3:')
print(p3)

