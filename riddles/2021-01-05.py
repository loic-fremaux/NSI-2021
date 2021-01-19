T = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]


def moyenne_tab(T) -> float:
    a = []
    for e in T:
        if isinstance(e, list):
            a.append(moyenne_tab(e))
        else:
            a.append(e)

    total = 0
    for e in a:
        total += e
    return total / len(a)


print(moyenne_tab(T))
