def sort_by_insertion(tab):
    n = len(tab)
    j = 0
    for i in range(1, n):
        key = tab[i]
        j += 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
