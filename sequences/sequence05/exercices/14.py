def est_premier(nb: int) -> bool:
    for i in range(2, nb):
        if nb % i == 0:
            return False
    return True


print(list(filter(lambda x: est_premier(x), [1, 2, 3, 4, 5, 7, 10, 11, 13, 17, 18])))
