def exchange(t):
    hour = (t // 3600) % 24
    minute = (t % 3600) // 60
    second = (t % 3600) % 60
    # Tính toán AM/PM
    am_pm = "AM" if hour < 12 else "PM"

    # Đổi giờ sang 12-hour format (không dùng câu điều kiện hay vòng lặp)
    hour_12 = hour % 12 or 12

    # Xuất kết quả
    print(f"{hour_12}:{minute}:{second} {am_pm}")

t = int(input("Nhập số giây: "))
exchange(t)

