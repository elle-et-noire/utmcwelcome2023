fibs = [1, 1]

def fibonacci(n):
    if n >= len(fibs) and (n != 0) and (n != 1):
        fibs.append(fibonacci(n - 1) + fibonacci(n - 2))
    return fibs[n]

for i in range(10):
    print(fibonacci(i))
