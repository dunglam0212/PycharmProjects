#Câu 1: Nhập một số từ người dùng và kiem tra xem số đó có là chẵn hay lẻ
x = int(input("Enter a number: "))
if x%2==0:
    print("Even")
else:
    print("Odd")

#Câu 2: Nhập một số từ người dùng và kiem tra xem là số âm hay dương
y = float(input("Enter a number: "))
if y>0:
    print("Số dương")
elif y<0:
    print("Số âm")
else:
    print("y là số 0, khong duong cung khong am")

#Cau 3: kiem tra xem so co chia hết cho 5 và 7 hay không
z = int(input("Enter a number: "))
if (z%5==0) and (z%7==0):
    print(f"({z} chia hết cho 5 và 7")
else:
    print(f"{z} không chia hết cho 5 và 7")

#Cau 5: viet chuong trinh kiem tra đăng nhập của 1 ng vào phần mềm
ten = "lamthuydung"
ten_dang_nhap = input("Nhập tên đăng nhập của bạn: ")
if ten_dang_nhap == ten:
    pass0 = "02122005"
    password = input("Nhập mật khẩu: ")
    if pass0==password:
        print("Bạn đã đăng nhập thành công!")
    else:
        print("Mật khẩu không chính xác!")
else:
    print("Tên đăng nhập không chính xác!")

#Cau 6: Xếp loại học sinh
diem = float(input("Hãy nhập điểm của bạn: "))
if diem <5:
    print("Yếu")
elif diem<6.5:
    print("Trung bình")
elif diem<8:
    print("Khá")
else:
    print("Giỏi")

