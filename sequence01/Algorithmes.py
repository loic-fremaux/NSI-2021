def seq_search(elt, tab):
    n = len(tab)
    i = 0
    while i < n and elt != tab[i]:
        i += 1
    return -1 if i == n else n


def average(tab):
    n = len(tab)
    s = 0
    for i in range(0, n - 1):
        s = s + tab[i]
    return s / n


def find_min(tab):
    n = len(tab)
    j = 0
    low = tab[0]
    for i in range(0, n - 1):
        if tab[j] < tab[low]:
            low = j
    return low


def sort_by_selection(tab):
    n = len(tab)
    for i in range(0, n - 1):
        low = i
        for j in range(i + 1, n - 1):
            if tab[j] < tab[low]:
                low = j
        if low != i:
            tab[low], tab[i] = tab[i], tab[low]


def sort_by_insertion(tab):
    n = len(tab)
    for i in range(1, n - 1):
        key = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key


def find_by_dichotomy(elt: int, tab):
    g, m = 0, 0
    d = len(tab)
    while g < d - 1:
        m = d + g // 2
        if elt < tab[m]:
            d = m
        else:
            g = m
    return g if tab[g] == elt else False


def return_change(money: int, tab):
    lst = []
    i = len(lst) - 1
    while money > 0:
        val = tab[i]
        if money < val:
            i = i - 1
        else:
            lst.append(val)
            money -= val

    return lst
