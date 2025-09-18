def fib(n):
    if n==0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = int(input("Enter a number:"))
print(fib(n))

#Alternate method
def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end = " ")
        a, b = b, b + a

n = int(input("Enter a number:"))
print(fib(n))