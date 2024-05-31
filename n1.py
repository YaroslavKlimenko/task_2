def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-2)+fib(n-1)
fib(int(input()))
print("Hello, World!")
