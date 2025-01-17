from QuanLyDiemSinhVien.models.Student import Student, tinh_dtb, ListStudent, xep_loai

student_database = ListStudent()

s1 = Student('K234111328', 'Lâm Thùy Dung', '01/12/2005', 'K23411', 7.0, 5.0, 7.5)
student_database.add_student(s1)
dtb_s1 = tinh_dtb(7.0,5.0,7.5)
s1.dtb = dtb_s1
s1.hl = xep_loai(dtb_s1)
print('Danh sách sinh viên: ')
print('ID\tNAME\tDATE OF BIRTH\tCLASS\tDQT\tDGK\tDCK\tDTB\tHOC LUC')
student_database.print_students()