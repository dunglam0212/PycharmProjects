def kiemtra(n):
    if n%2==1 or n%2==0:
        S=0
        for i in range(1,int(n/2)+1):
            if n%i==0:
                S=S+i
        if S==n:
            return 1
    return 0
n=int(input('Nhập: '))
for i in range(1,n+1):
    if kiemtra(i)==1:
        print(i)
#Vấn đề: Tìm các số hoàn thiện trong khoảng từ 1 tới n bất kỳ