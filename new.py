def fibonacci_1(n):
    print(f'fib{n}')
    if n <= 0:
        print("Incorrect input")
    elif n <= 2:
        return 1
    else:
        return fibonacci_1(n - 1) + fibonacci_1(n - 2)

print(fibonacci_1(6))