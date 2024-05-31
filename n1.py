def fib(n):
    a1=0
    a2=1
    for i in range(n):
        print(a1)
        x=a1
        a1=a2
        a2=a1+x
fib(int(input()))
print("Hello, World!")
