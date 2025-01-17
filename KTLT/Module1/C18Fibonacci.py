def fib(x):
    if x==1 or x==2:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print(fib(8))

def fib_list(x):
    for i in range(1,x):
        print(fib(i), end='->')
    print(fib(x))

fib_list(9)

#Khử đệ quy
def fibo(n):
    fibo_list = []
    for i in range(n):
        if i==0 or i==1:
            fibo_list.append(1)
        else:
            fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    return fibo_list[n-1], fibo_list

fibo_x, list = fibo(8)
#fibo_x là lấy vị trí thứ 8 trong dãy fibonacci
#Còn list là trả về dãy số fibonacci tính từ 1 cho đến vị trí thứ 8
print('Vị trí thứ 8 trong dãy fibonacci là: ',fibo_x)
print('Dãy fibonacci tính từ 1 đến vị trí thứ 8 là: ', list)


