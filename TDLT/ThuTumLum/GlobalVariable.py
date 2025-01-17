g=5
def increment():
    """g trong hàm này là biến local, không liên quan gì đến biến global g=5"""
    g=2
    g=g+1
    print("Local Variable:",g)
increment()
print("Global Variable:",g)

g=5
def increment():
    global g
    print("Global Variable:",g)
    """Lúc này, mình có thể tác động đến biến global g, các lệnh ở trong 
hàm vẫn ảnh hưởng đến biến global g => xuất giá trị = 3"""
    g=2
    g=g+1
    print("Local Variable:",g)
increment()
print(g)

g=5
def increment():
    """Lúc này, hệ thống báo lỗi do không biết biến g (tron g+1) là ở đâu ra
    Do g=5 - biến global độc lập với biến local trong hàm"""
    g=g+1
increment()
print(g)