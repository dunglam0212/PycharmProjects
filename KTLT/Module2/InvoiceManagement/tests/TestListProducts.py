from Module2.InvoiceManagement.lib.ListProduct import *
from Module2.InvoiceManagement.lib.Product import Product

List_Products = ListProduct()
p1 = Product("P1","Thuốc chống khùng", "Cái", 30,100)
p2 = Product("P2","Thuốc chống Phan Ngọc", "Cái", 15,346)
p3 = Product("P3","Thuốc 1", "Cái", 45,34)
p4 = Product("P4","Thuốc 2", "Cái", 36,76)
p5 = Product("P5","Thuốc 3", "Cái", 65,45)

List_Products.add_product(p1)
List_Products.add_product(p2)
List_Products.add_product(p3)
List_Products.add_product(p4)
List_Products.add_product(p5)

List_Products.print_list_products()
find_id = "P3"
rs = List_Products.find_product_by_id(find_id)
if rs == None:
    print(f"Không tìm thấy sản phẩm nào có mã {find_id}")
else:
    print(f"Đã tìm thấy sản phẩm có mã {find_id}")

find_name = "Thuốc chống khùng"
rs1 = List_Products.find_product_by_name(find_name)
if rs1 == None:
    print(f"Không tìm thấy sản phẩm nào có tên {find_name}")
else:
    print(f"Đã tìm thấy sản phẩm có tên {find_name}")

remove_id = "P4"
rs2 = List_Products.remove_product_by_id(remove_id)
if rs2 == None:
    print(f"Không tìm thấy sản phẩm có mã {remove_id} để xoá")
else:
    print(f"Đã xoá thành công sản phẩm có mã {remove_id}")
    print(f"Danh sách sách sản phẩm sau khi xoá là:")
    List_Products.print_list_products()

List_Products.order_by_price_asc()
print("Danh sách sản phẩm sau khi sắp xếp theo giá tăng dần là:")
List_Products.print_list_products()

rs = List_Products.filter_price(40,120)
print("Danh sách sản phẩm có giá nằm trong khoảng 40 đến 120 là")
for p in rs:
    print(p)