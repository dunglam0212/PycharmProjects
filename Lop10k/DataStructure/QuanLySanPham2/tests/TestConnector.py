from DataStructure.connector.Connector import Connector

myconnector = Connector()
myconnector.connect() #không truyền đối số nào cả -> tức là lấy thông số kết nối mặc định
cursor = myconnector.conn.cursor()
sql = 'select * from employee'
cursor.execute(sql)
dataset_employee = cursor.fetchall() #đọc toàn bộ dữ liệu Employee
for record in dataset_employee:
    id=record[0]
    name=record[1]
    print(id, name)
cursor.close()

#truy vấn lấy thông tin chi tiết của Employee khi biết id
sql1 = "select * from employee where id=2"
cursor1 = myconnector.query(sql1)
dataset1 = cursor1.fetchone()
if dataset1!=None:
    id, name, username, password=dataset1
    print('Name=', name)
    print('password=', password)
cursor1.close()

#Minh họa đăng nhập hệ thống:
sql_login = "select * from employee where username=%s and password=%s"
val_input=("admin5", "123")
cursor_login = myconnector.conn.cursor()
cursor_login.execute(sql_login, val_input)
dataset_login = cursor_login.fetchone()
if dataset_login!=None:
    id, name, username, password = dataset_login
    print('name=', name)
    print('password=', password)
else:
    print('Đăng nhập thất bại!!!')