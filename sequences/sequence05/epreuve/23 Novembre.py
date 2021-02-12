from typing import List


def minimum(tab: List[int]) -> int:
    """
    Prend en paramètre une List d'int tab et renvoie le plus petit de ses nombres
    :param tab: List[int]
    :return: int
    """
    if len(tab) == 0:
        return -1

    low = tab[0]
    for i in range(1, len(tab)):
        if tab[i] < low:
            low = tab[i]
    return low


# TESTS
print(minimum([]))
print(minimum([0, 1, 2]))
print(minimum([3, 5, 1, 4]))
print(minimum([3, 5, 3, 4]))
