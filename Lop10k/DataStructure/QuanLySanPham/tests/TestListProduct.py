#Khởi tạo 1 danh sách rỗng để lưu các product
from DataStructure.QuanLySanPham.models.Product import Product

products=[]
#thêm 1 sản phẩm
products.append(Product('p1', 'Coca',15,30))
products.append(Product('p2', 'Pepsi',7,35))
products.append(Product('p3', 'Fanta',20,12))
products.append(Product('p4', '7Up',26,37))

print('Danh sách sản phẩm: ')
for product in products:
    print(product)
print('-'*30)
print('Danh sách sản phẩm đã có STT')
for i in range(len(products)):
    product = products[i]
    print(f"{i+1}", end='\t') #i+1 vì thông thường STT thì bắt đầu từ số 1
    print(product)
#Hãy viết hàm lọc ra tất cả product có giá từ min tới max
def filter_products(min_price, max_price):
    products_filter = []
    for product in products:
        if product.price >= min_price and product.price <= max_price:
            products_filter.append(product)
    return products_filter

results = filter_products(30,40)
print('Danh sách sản phẩm sau khi lọc giá từ 30 đến 40:')
for product in results:
    print(product)

#Viết hàm xóa sản phẩm có mã bất kỳ nhập vào từ bàn phím
#Nếu tìm kh thấy mã thì bảo là không thấy
#hoặc: xóa thành công là True, xóa thất bại là False
def delete_products(id_delete):
    #Bước 1: Tìm xem id_delete có tồn tại trong products hay không
    p_found = None
    for product in products:
        if product.id == id_delete:
            p_found = product
            break #Tìm thấy thì dừng vòng lặp
    if p_found == None:
        return False #Không tìm thấy sản phẩm nào có mã là id_delete tồn tại trong products
    products.remove(p_found)
    return True #Xóa thành công
print('-'*30)
print('----Danh sách toàn bộ sản phẩm----')
for product in products:
    print(product)
id_delete = input('Mời bạn nhập vào mã sản phẩm muốn xóa: ')
result = delete_products(id_delete)
if result == True:
    print('Đã xóa thành công sản phẩm có mã = ', id_delete)
    for product in products:
        print(product)
else:
    print('Không tìm thấy sản phẩm nào có mã = ', id_delete, 'để xóa')


