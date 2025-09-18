def inf_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, b + a

f = inf_fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))