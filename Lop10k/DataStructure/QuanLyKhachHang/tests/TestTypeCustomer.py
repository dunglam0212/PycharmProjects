from DataStructure.QuanLyKhachHang.models.TypeCustomer import TypeCustomer

def print_type_customer(tc):
    print(type(tc))
    print(tc.name)
    print(tc.value)

tc1 = TypeCustomer.VIP
print_type_customer(tc1)
'''print(type(tc1))
print(tc1.name)
print(tc1.value)'''

tc1 = TypeCustomer.POTENTIAL
print_type_customer(tc1)
