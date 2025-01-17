import mysql.connector

server = "localhost"
port = 3306
database = "employeemanagement"
username = "root"
password = "dungcute0212"

conn = mysql.connector.connect(
                host=server,
                port=port,
                database = database,
                user=username,
                password=password
            )
cursor = conn.cursor()
sql = "SELECT * FROM employee"
cursor.execute(sql)
dataset = cursor.fetchall()
print(dataset)