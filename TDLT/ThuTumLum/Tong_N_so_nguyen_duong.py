N = int(input("Nhập vào số nguyên dương N: "))
if N > 0:
    i = 1
    s = 0
    if i < N:
        i = i + 1
        s = s + i #Cần học cấu trúc lặp để thực hiện bài này
    else:
        s = s + i
        print("Tổng các số nguyên dương từ 1 đến N =",s)
else:
    print("Thông tin bạn nhập không hợp lệ!")