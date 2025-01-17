print("Hãy nhập tên của bạn:")
ten = input()
print("Tên của bạn là:",ten)

print("Hãy nhập điểm trung bình của bạn:")
dtb=float(input())
print("Điểm trung bình của bạn là:",dtb)

def StrToBool(x):
    return x.lower() in ("Đúng", "True", "Yes", "có", "y", "1", "t")
print("Bạn có thích môn Toán không?")
x = StrToBool(input())
print("Câu trả lời của bạn là",x)

age = int(input("Hãy nhập tuổi của bạn: "))
print("15 năm sau, tuổi của bạn sẽ là:", age+15)

