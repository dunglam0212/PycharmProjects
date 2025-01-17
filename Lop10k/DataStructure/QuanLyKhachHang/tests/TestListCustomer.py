from DataStructure.QuanLyKhachHang.models.Customer import Customer
from DataStructure.QuanLyKhachHang.models.ListCustomer import ListCustomer
from DataStructure.QuanLyKhachHang.models.TypeCustomer import TypeCustomer
from DataStructure.QuanLyKhachHang.models.TypePhone import TypePhone

customer_database = ListCustomer()
c1=Customer('c1','Obama','obama@gmail.com','0939846542',28,TypeCustomer.VIP)

customer_database.add_customer(c1)

c2=Customer('c2','Putin','putin@gmail.com','0973844754',35,TypeCustomer.POTENTIAL)
customer_database.add_customer(c2)

c3=Customer('c3','Trump','trump@gmail.com','0939254642',30,TypeCustomer.NORMAl)
customer_database.add_customer(c3)

c4=Customer('c4','Kim Un','trump@gmail.com','0982364764',39,TypeCustomer.NORMAl)
customer_database.add_customer(c4)

c5=Customer('c5','Lisa','lisa@gmail.com','0937456442',17,TypeCustomer.POTENTIAL)
customer_database.add_customer(c5)

c6=Customer('c6','Rose','rose@gmail.com','0986472452',26,TypeCustomer.VIP)
customer_database.add_customer(c6)

c7=Customer('c7','Jenny','jenny@gmail.com','0903532482',27,TypeCustomer.NORMAl)
customer_database.add_customer(c7)

c8=Customer('c8','Jisoo','jisoo@gmail.com','0973465642',24,TypeCustomer.VIP)
customer_database.add_customer(c8)

print('Danh sách khách hàng: ')
customer_database.print_customers()

print('Thống kê khách hàng VIP:')
filter_vip_customer = customer_database.filter_type_customers(TypeCustomer.VIP)
for c in filter_vip_customer:
    print(c)
print(f'==>Có {len(filter_vip_customer)} khách hàng VIP')

print('Thống kê khách hàng thường: ')
filter_normal_customer = customer_database.filter_type_customers(TypeCustomer.NORMAl)
for c in filter_normal_customer:
    print(c)
print(f'==> Có {len(filter_normal_customer)} khách hàng thường')

#Hãy viết hàm lọc ra các khách hàng có trong độ tuổi nòa đó
filter_age_customers = customer_database.filter_age_customers(20,30)
print('Các khách hàng có độ tuổi từ 20 đến 30: ')
filter_age_customers.print_customers()

#Hãy lọc số điện thoại với đầu các hãng đth
filter_viettel = customer_database.filter_type_phone_customers(TypePhone.VIETTEL)
print('Danh sách các khách hàng sử dụng nhà mạng Viettel:')
filter_viettel.print_customers()

filter_mobi = customer_database.filter_type_phone_customers(TypePhone.MOBI)
print('Danh sách các khách hàng sử dụng nhà mạng Mobi:')
filter_mobi.print_customers()

filter_vina = customer_database.filter_type_phone_customers(TypePhone.VINA)
print('Danh sách các khách hàng sử dụng nhà mạng Vina:')
filter_vina.print_customers()

#Sắp xếp các khách hàng theo độ tuổi giảm dần
customer_database.sort_customer_age_dsc()
print('Danh sách khách hàng sắp xếp theo độ tuổi giảm dần: ')
customer_database.print_customers()

#Tìm khách hàng (Tìm tuyệt đối)
id = input('Nhập mã khách hàng muốn tìm: ')
find_cust = customer_database.find_1_id(id)
if find_cust == None:
    print(f'Không tìm thấy khách hàng có mã là {id}')
else:
    print(f'Đã tìm thấy khách hàng có mã là {id}')
    print('Thông tin chi tiết của khách hàng có mã là: ', id)
    print(find_cust)
    print(find_cust.get_details())
    find_cust.name = 'Hihi'
print('-'*10)
print('Xuất lại danh sách khách hàng:')
customer_database.print_customers()
print('-'*30)
c9 = Customer('c9','Haha','haha@gmail.com','09082348642',30,TypeCustomer.VIP)
customer_database.update_customer(3, c9)
print('Danh sách khách hàng sau khi thay thế: ')
customer_database.print_customers()

print('-'*30)
customer_database.remove_customer_by_index(3)
print('Danh sách khách hàng sau khi xóa index = 3: ')
customer_database.print_customers()

print('-'*30)
remove_id = 'c3'
rs = customer_database.remove_customer_by_id(remove_id)
print('Danh sách khách hàng sau khi xóa id =', remove_id)
if rs == True:
    print(f'Xóa khách hàng có mã {remove_id} thành công!')
    customer_database.print_customers()
else:
    print(f'Xóa khách hàng có mã {remove_id} thất bại!')