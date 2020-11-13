def multi(a, b):
    return self_addition(a, a, b)


def self_addition(a, b, n):
    if n == 1:
        return a
    else:
        return self_addition(a + b, b, n - 1)


print(multi(3, 10))
