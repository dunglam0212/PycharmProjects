
from QuanLySanPham2.models import ListProduct, Product


database = ListProduct()
#Them 1 product mới:
database.add_product(Product('P1','áo ấm',3,150))
database.add_product(Product('P2','áo gió',5,200))
database.add_product(Product('P3','áo len',10,80))
p = Product('P4','Áo 3 lỗ',8,10)
database.add_product(p)
database.add_product(Product('P5','áo thun',2,70))


print('Danh sách sản phẩm trong cơ sở dữ liệu:')
print('ID\tNAME\tQUANTITY\tPRICE')
database.print_products()


#cách 1
min_price = 80
max_price = 200
print('Danh sách các sản phẩm có giá từ 80 đến 200:')
result = database.filter_products(min_price,max_price)
for p in result:
    print(p)

#Cách 2
min_price = 80
max_price = 100
print('Danh sách các sản phẩm có giá từ 80 đến 100:')
result = database.filter_list_product(min_price, max_price)
result.print_products()

#Tìm sản phẩm
id_search = 'P3'
p_found = database.find_product_by_id(id_search)
if p_found == None:
    print('Tìm đỏ mắt không thấy sản phẩm nào trong kho có mã =', id_search)
else:
    print(f'Đã tìm thấy trong kho có sp có mã = {id_search}')
    print('Thông tin chi tiết của sp này là:', p_found)

id_remove = input('Bạn muốn xóa sp có mã=')
rs = database.remove_product_by_id(id_remove)
if rs==False:
    print('Xóa sp có mã =', id_remove, 'thất bại')
else:
    print('Xóa sp có mã ', id_remove, 'thành công')
    print('Danh sách sp sau khi xóa', id_remove)
    database.print_products()

print('Danh sách sp theo đơn giá tăng dần: ')
database.sort_product_price_asc()
database.print_products()
print()
print('Danh sách sau khi thêm sp có giá bằng nhau: ')
#C1: Thêm 1 product có giá trùng nhau
p6 = Product('P6', 'T-shirt', 34, 80)
database.add_product(p6)
database.print_products()
#C2: Sắp xếp sp theo giá giảm dần, nếu giá sp bằng nhau thì sắp xếp theo số lượng tăng dần
print('Danh sách sau khi sắp xếp giảm dần: ')
database.sort_product_price_dsc()
database.print_products()
