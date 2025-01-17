def funX(m,n1=2,n2=4):
    sum=n1+n2
    for i in range(1,m):
        sum=sum+i
    return sum

s1=funX(5)
print(f's1 = {s1}')
s2=funX(5,3)
print(f's2 = {s2}')
s3=funX(5,3,2)
print(f's3 = {s3}')
