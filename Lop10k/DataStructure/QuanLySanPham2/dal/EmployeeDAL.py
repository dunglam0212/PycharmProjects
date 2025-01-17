from DataStructure.QuanLySanPham2.models.Employee import Employee
from DataStructure.connector.Connector import Connector


class EmployeeDAL(Connector):
    def get_list_employees(self):
        sql = "select * from employee"
        cursor = self.query(sql)
        dataset = cursor.fetchall()
        employees=[]
        for record in dataset:
            id=record[0]
            name=record[1]
            username=record[2]
            password=record[3]
            emp=Employee(id, name, username, password)
            employees.append(emp)
        cursor.close()
        return employees
    def get_detail_employee_by_id(self, id):
        sql = f"select * from employee where id={id}"
        cursor=self.query(sql)
        dataset = cursor.fetchone()
        if dataset!=None:
            id, name, username, password = dataset
            emp = Employee(id, name, username, password)
        else:
            emp=None
        cursor.close()
        return emp
    def login(self, username, password):
        sql_login = "select * from employee where username=%s and password=%s"
        val_input = (username, password)
        cursor = self.query(sql_login, val_input)
        dataset = cursor.fetchone()
        if dataset!=None:
            id, name, username, password = dataset
            emp = Employee(id, name, username, password)
        else:
            emp = None
        cursor.close()
        return emp
    def changepassword(self, id, new_pass):
        sql = "update employee set password=%s where id=%s"
        val_input = (new_pass, id)
        cursor = self.query(sql, val_input)
        self.conn.commit() #xác thực thay đổi dữ liệu
        return cursor.rowcount #trả về số dòng bị thay đổi trong csdl
