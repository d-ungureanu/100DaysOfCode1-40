def add(*args):
    numbers_sum = 0
    for number in args:
        numbers_sum += number
    return numbers_sum


print(add(1, 2, 3, 4, 5))
print(add(10, 12))


def calculate(n, **kwargs):
    print(kwargs)
    if kwargs.get("add") is not None:
        n += kwargs.get("add")
    n *= kwargs.get("multiply")
    print("n after operations: ", n)


calculate(2, multiply=5)
