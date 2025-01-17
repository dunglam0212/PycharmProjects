from DataStructure.QuanLySanPham2.dal.EmployeeDAL import EmployeeDAL

employee_dal = EmployeeDAL()
employee_dal.connect()
list_emp = employee_dal.get_list_employees()
for emp in list_emp:
    print(emp.id, emp.name, emp.username, emp.password)

#Test lấy thông tin chi tiết của Employee bất kỳ
emp = employee_dal.get_detail_employee_by_id(2)
if emp!=None:
    print("Tìm thấy employee có mã id = 2")
    print('Thông tin chi tiết')
    print(emp.id, emp.name, emp.username, emp.password)
else:
    print("Không tìm thấy employee có id =", id)

#Test đăng nhập hệ thống
emp = employee_dal.login("hong", "4567")
if emp!=None:
    print('Đăng nhập thành công!')
else:
    print("Đăng nhập thất bại, vui lòng kiểm tra lại thông tin đăng nhập")

#Test đổi mật khẩu
id = 2
new_pass = "haha"
emp = employee_dal.changepassword(id, new_pass)
print(emp)
