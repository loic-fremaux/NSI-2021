print("--------------------------")


def seq_search(elt, tab):
    """
    Find an element elt in an array tab and returns its index.
    If the array doesn't contains the element, returns -1

    :param elt: the element to search
    :param tab: the array
    :return: the index of the element or -1
    """
    n = len(tab)
    i = 0
    while i < n and elt != tab[i]:
        i += 1
    return -1 if i == n else i


print("------- seq_search -------")
print("Trying to search 5 in [1, 3, 5, 7, 9], expected result is 2")
print("Result: ", seq_search(5, [1, 3, 5, 7, 9]))
print("Trying to search 13 in [3, 4, 5, 10, 13], expected result is 4")
print("Result: ", seq_search(13, [3, 4, 5, 10, 13]))
print("Trying to search 1 in [1, 3, 5, 7, 9], expected result is 0")
print("Result: ", seq_search(1, [1, 3, 5, 7, 9]))


def average(tab):
    """
    Get the average value of an array

    :param tab: the array
    :return: the average of the array
    """
    n = len(tab)
    s = 0
    for i in range(0, n):
        s = s + tab[i]
    return s / n


print("--------- average --------")
print("Trying to do the average of [1, 3, 5, 7, 9], expected result is 5")
print("Result: ", average([1, 3, 5, 7, 9]))
print("Trying to do the average of [1, 2, 4, 5, 8, 10], expected result is 5")
print("Result: ", average([1, 2, 4, 5, 8, 10]))


def find_min(tab):
    """
    Find the smallest value of an array

    :param tab: the array
    :return: the smallest value
    """
    n = len(tab)
    low = tab[0]
    for i in range(0, n - 1):
        if tab[i] < low:
            low = tab[i]
    return low


print("-------- find_min --------")
print("Trying with [3, 7, 12, 2, 7, 19], expected result is 2")
print("Result: ", find_min([3, 7, 12, 2, 7, 19]))


def sort_by_selection(tab):
    """
    Sort an array using the selection method

    :param tab: the array to sort
    :return: the sorted array
    """
    n = len(tab)
    for i in range(0, n - 1):
        low = i
        for j in range(i + 1, n - 1):
            if tab[j] < tab[low]:
                low = j
        if low != i:
            tab[low], tab[i] = tab[i], tab[low]
    return tab


print("--- sort_by_selection ----")
print("Trying with [3, 8, 1, 2, 5, 0, 8, 1, 1, 2, 14], expected result is [0, 1, 1, 1, 2, 2, 3, 5, 8, 8, 14]")
print("Result: ", sort_by_selection([3, 8, 1, 2, 5, 0, 8, 1, 1, 2, 14]))


def sort_by_insertion(tab):
    """
    Sort an array using the insertion method

    :param tab: the array to sort
    :return: the sorted array
    """
    n = len(tab)
    for i in range(1, n - 1):
        key = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab


print("--- sort_by_insertion ----")
print("Trying with [3, 8, 1, 2, 5, 0, 8, 1, 1, 2, 14], expected result is [0, 1, 1, 1, 2, 2, 3, 5, 8, 8, 14]")
print("Result: ", sort_by_insertion([3, 8, 1, 2, 5, 0, 8, 1, 1, 2, 14]))


def find_by_dichotomy(elt: int, tab):
    """
    Find an element in an array using the dichotomy method

    :param elt: the element to search
    :param tab: the array
    :return: the element or False if it was not found
    """
    g, m = 0, 0
    d = len(tab)
    while g < d - 1:
        m = (d + g) // 2
        if elt < tab[m]:
            d = m
        else:
            g = m
    return g if tab[g] == elt else False


print("---- find_by_dichotomy ---")
print("Trying to search 5 in [1, 3, 5, 7, 9], expected result is 2")
print("Result: ", find_by_dichotomy(5, [1, 3, 5, 7, 9]))
print("Trying to search 13 in [3, 4, 5, 10, 13], expected result is 4")
print("Result: ", find_by_dichotomy(13, [3, 4, 5, 10, 13]))
print("Trying to search 1 in [1, 3, 5, 7, 9], expected result is False")
print("Result: ", find_by_dichotomy(13, [1, 3, 5, 7, 9]))


def return_change(money: int, tab):
    """
    convert a sum of money into a number of bills and coins according to the monetary system

    :param money: the sum of money to convert
    :param tab: the monetary system
    :return: the bills and coins to return
    """
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


print("------ return_change -----")
print("Trying to convert 133 with [1, 2, 5, 10, 20, 50, 100, 200, 500], expected result is [100, 20, 10, 2, 1]")
print("Result: ", return_change(133, [1, 2, 5, 10, 20, 50, 100, 200, 500]))
print("--------------------------")
