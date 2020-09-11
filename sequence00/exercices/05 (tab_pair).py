def tab_pair(n):
    """
    takes as a parameter an array of numbers and returns all even numbers below it
    :param n: the greatest value
    :return: an array of numbers and returns all even numbers below it
    """
    tab = []
    for i in range(0, n + 1, 2):
        tab.append(i)
    return tab


print(tab_pair(13))
print(tab_pair(14))
