def fib():
    a, b = 1, 1

    while a < 100:
        yield a
        a, b = b, a + b


for f in fib():
    print(f)
