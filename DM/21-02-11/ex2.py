import random


def tri_bulles(T: list) -> list:
    n = len(T)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if T[j] > T[j + 1]:
                temp = T[j]
                T[j] = T[j + 1]
                T[j + 1] = temp

    return T


print(tri_bulles(random.sample(range(0, 100), 10)))


def tri_bulles2(T: list) -> list:
    n = len(T)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if T[j] > T[j + 1]:
                temp = T[j]
                T[j] = T[j + 1]
                T[j + 1] = temp

    return T


print(tri_bulles2(random.sample(range(0, 100), 10)))
