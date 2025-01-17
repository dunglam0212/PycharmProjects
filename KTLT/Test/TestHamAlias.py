#Hàm cong0 thì c và pskq cùng trỏ tới cùng 1 ô nhớ
#Khi pskq thay đổi thì giá trị của c cũng thay đổi theo
#các giá trị do mình định nghĩa lại thì có thể bị thay đổi
def cong0(ps1, ps2, pskq):
    pskq[0] = ps1[0]*ps2[1] + ps2[0]*ps1[1]
    pskq[1] = ps1[1]*ps2[1]
a=[1,2]
b=[3,5]
c=[0,1]
cong0(a,b,c)
print(c)

#Hàm tổng ở dưới đây do z được gán cho 1 giá trị nên khi chạy dòng 20 thì z=7
def tong(a,b,c):
    c=a+b
x=6
y=6
z=7
tong(x,y,z)
print(z)