import mysql.connector

server = 'localhost'
port = 3306
database = 'studentmanagement'
username = 'root'
password = 'dungcute0212'

conn = mysql.connector.connect(
    host = server,
    port = port,
    database = database,
    user = username,
    password = password
)

#Truy vấn toàn bộ sinh viên từ cơ sở dữ liệu
#sql = 'select * from student'
#Truy vấn các sinh viên có độ tuổi từ 18 đến 19
#sql = 'SELECT * FROM student where Age >=18 and Age<=19'

'''#truy vấn toàn bộ sinh viên và sắp xếp theo độ tuổi tăng dần
sql = 'SELECT * FROM student ' \
    'order by Age asc'

#truy vấn sinh viên có độ tuổi từ 18 đến 19 và sắp xếp theo độ tuổi giảm dần
sql = 'SELECT * FROM student ' \
    'where Age>=18 and Age<=19 ' \
    'order by Age desc'

#truy vấn chi tiết sinh viên khi biết ID=1
sql = 'SELECT * FROM student ' \
    'where ID=1'

#truy vấn dạng phân trang (paging) student
sql = 'SELECT * FROM student LIMIT 3 OFFSET 0'
sql = 'SELECT * FROM student LIMIT 3 OFFSET 3'
#LIMIT: số phần tử mà ta muốn truy vấn
#OFFSET: vị trí ta bắt đầu truy vấn
cursor.execute(sql)

dataset = cursor.fetchall()
align = '{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code', 'Name', 'Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id, code, name, age))

cursor.close()'''

'''#Thêm mới 1 student
cursor = conn.cursor()
sql1 = 'insert into student (code, name, age) values (%s, %s, %s)'
val = ('sv06', 'Jack', 37)
cursor.execute(sql1, val)
conn.commit()
print(cursor.rowcount, 'record inserted')

#Thêm mới nhiều student
cursor = conn.cursor()
sql2 = 'insert into student (code,name,age) values (%s,%s,%s)'
val2 = [
    ("sv07", "Jurgen",21),
    ("sv08","Shally",22),
    ("sv09","Marine",24),
]
cursor.executemany(sql2, val2)
conn.commit()
print(cursor.rowcount, 'record inserted')'''

'''#Cậpnhật tên sv có code='sv09'
cursor = conn.cursor()
sql = "update student set name = 'Marry' where Code='sv09'"
cursor.execute(sql)

conn.commit()

print(cursor.rowcount, ' record(s) affected')'''

'''#Cập nhập tên sv như trên nhưng dưới dạng SQL Injection
cursor = conn.cursor()
sql = "update student set name=%s where Code=%s"
val = ('Anna', 'sv09')
cursor.execute(sql, val)
conn.commit()
print(cursor.rowcount, ' record(s) affected')'''

'''#Xóa student có ID=5
cursor = conn.cursor()
sql = "DELETE from student where ID=5"
cursor.execute(sql)
conn.commit()
print(cursor.rowcount, ' record(s) affected')'''

#Xóa student có ID=3 với SQL Injection
cursor = conn.cursor()
sql = "DELETE from student where ID=%s"
val=(3,)
cursor.execute(sql, val)
conn.commit()
print(cursor.rowcount, ' record(s) affected')

