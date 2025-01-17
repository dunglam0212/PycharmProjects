TN = float(input("Hãy nhập tổng thu nhập tính thuế theo năm (triệu đồng) của bạn: "))
if TN > 0:
    if TN <= 60:
        TS = 0.05
    elif TN <= 120:
        TS = 0.1
    elif TN <= 216:
        TS = 0.15
    elif TN <= 384:
        TS = 0.2
    elif TN <= 624:
        TS = 0.25
    elif TN <= 960:
        TS = 0.3
    else:
        TS = 0.35
    print("Thuế thu nhập cá nhân của bạn là:", TS)
else:
    print("Thông tin bạn nhập không hợp lệ!")
