def est_premier(n):
    """
    check if a number is a prime number
    :param n: the number to check
    :return: True if the number is a prime number or else False
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for i in range(10, 101):
    iStr = str(i)
    j = ""
    for k in range(len(iStr) - 1, -1, -1):
        j += iStr[k]
    if est_premier(i) and est_premier(int(j)):
        print(i)