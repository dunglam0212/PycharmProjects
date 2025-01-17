def calAverage(t,l,h):
    dtb = (t+l+h)/3
    return dtb

#kiểm thử
t=5
l=2
h=9
dtb=calAverage(t,l,h)
print("Điểm trung bình là:",dtb)

def ptb1(a,b):
    if a==0 and b==0:
        return "Vô số nghiệm"
    elif a==0 and b!=0:
        return "Vô nghiệm"
    else:
        x = -b/a
        return f"Nghiệm = {x}"

kq1 = ptb1(5,8)
print("Kêt quả của phương trình là",kq1)
