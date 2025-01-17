def factorial_non_recursive(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i #Giống như: fact = fact*i
    return fact

def factorial_recursive(n):
    if n == 0:
        return 1
    else:  #Không có else cũm được
        return n*factorial_recursive(n-1)

def A(n,k):
    return factorial_recursive(n)/factorial_recursive(n-k)
def C(n,k):
    return A(n,k)/factorial_recursive(k)

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)