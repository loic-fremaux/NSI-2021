def sort_by_selection(tab):
    n = len(tab)
    for i in range(n):
        low = i
        for j in range(i + 1, n):
            if tab[j] < tab[low]:
                low = j
        tab[i], tab[low] = tab[low], tab[i]
