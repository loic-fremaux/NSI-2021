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


print(est_premier(7))
print(est_premier(13))
print(est_premier(14))
