from Module3_Object.List_Student import ListStudent
from Module3_Object.Student import Student

ls = ListStudent()
ls.append_student(Student("Sv1", "Teo", 19))
ls.append_student(Student("Sv2", "Ti", 20))
ls.append_student(Student("Sv3", "Han", 25))
ls.append_student(Student("Sv4", "Ngoc", 15))
ls.append_student(Student("Sv5", "Mai", 36))
print("Danh sách sinh viên là:")
#gọi hành vi/phương thức xuất danh sách
ls.print_students()