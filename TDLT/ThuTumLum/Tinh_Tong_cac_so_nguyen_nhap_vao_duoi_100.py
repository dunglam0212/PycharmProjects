#Bài toán yêu cầu tính tổng các số nguyên nhập vào từ bàn phím cho đến khi tổng >100 thì dừng
'''total = 0
while True:
    try:
        num=int(input("Nhập một số nguyên: "))
        total+=num
        if total>100:
            print("Tổng các số nguyên đã nhập là:", total)
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")
print("Tổng các số nguyên đã nhập là:", total)
'''
def sum(n):
    i = 1
    s = 0
    while s <= 100:
        s = s + i
        i = i + 1
    return s
print(sum())
