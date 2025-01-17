from Module3_Object.Student import Student

sv1 = Student("SV1", "Teo", 19) #tự động gọi init
print("Thông tin chi tiết sinh viên:")
print(sv1)
#tự động gọi str

#để truy suất dữ liệu cho từng thuộc tính:
print("Mã sinh viên viên = ", sv1.id)
print("Tên sinh viên = ", sv1.name)
print("Tuổi sinh viên = ", sv1.age)