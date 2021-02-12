def insert(tab: list, elt, i: int):
    l = len(tab)
    tab.append(tab[-1])
    c = l
    while c != i:
        tab[c] = tab[c - 1]
        c -= 1
    tab[c] = elt


T = [1, 2, 3, 5]
insert(T, 4, 3)
print(T)
