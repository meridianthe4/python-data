# Q. 5. Create a infinite series on fib numbers and print first few

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()

print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))