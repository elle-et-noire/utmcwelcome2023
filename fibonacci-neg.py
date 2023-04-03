def fibonacci(n):
    if (n == 0) or (n == 1):
        return 1
    if n > 0:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci(n + 2) - fibonacci(n + 1)

for i in range(-10, 10):
    print(fibonacci(i))
