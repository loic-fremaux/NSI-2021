from functools import reduce


def fact(k): return reduce(lambda a, b: a * b, [i for i in range(1, k + 1)])


print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
