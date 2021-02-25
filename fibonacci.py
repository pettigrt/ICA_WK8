
def fib(x):
    if x < 0:
        print("Value must be positive")
        return 0
        
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        x = fib(x - 2) + fib(x - 1)

    return x


def factorial(x):
    if x < 0:
        print("Number must be positive")
        return 0

    if (x == 0):
        return 1
    elif x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(3))
print(factorial(4))
print(factorial(5))
    