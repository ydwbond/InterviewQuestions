memo = {0: 0}
FibArray = []


def memorize_decor(func):
    def wrapper(arg):
        func(arg)
    return wrapper


def memorize_decor_1(func):
    def wrapper(arg):
        print(arg)
    return wrapper



@memorize_decor
def fibonacci_1(n):

    if n <= 0:
        print("Incorrect input")
    elif n <= 2:
        return 1
    else:
        return fibonacci_1(n - 1) + fibonacci_1(n - 2)


print(fibonacci_1(5))

