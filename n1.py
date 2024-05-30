def fib(n):
    if n<3:
        return 1
    return fib(n-1)+fib(n-2)
print("Hello, World!")
n=int(input())
print(fib(n))
