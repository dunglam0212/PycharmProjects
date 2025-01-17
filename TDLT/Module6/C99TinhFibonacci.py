def list_fib(n):
    fib=[1,1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
print(list_fib(6))

def so_hang_fib(n):
    fib=[1,1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n-1]
print(so_hang_fib(6))