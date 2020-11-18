from typing import List


def recherche1(elt: int, tab: List[int]) -> List[int]: return [i for i in range(len(tab)) if tab[i] == elt]


print(recherche1(1, [1, 2, 3]))
print(recherche1(4, [1, 2, 3]))
