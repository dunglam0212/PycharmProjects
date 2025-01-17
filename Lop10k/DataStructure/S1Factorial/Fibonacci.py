def fibo(n):
    if n==1 or n==2:
        return 1
    return fibo(n-1) + fibo(n-2)

def list_fib(n):
    for i in range(1, n+1):
        f = fibo(i)
        print(f, end=' ')
    print()

