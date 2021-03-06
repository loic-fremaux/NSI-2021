def est_divisible(n, m):
    """
    check if a number is divisible by an other number
    :param n: the number to divide
    :param m: the number to divide by
    :return: True if the n is divisible by m
    """
    return n % m == 0


print("15 est divisible par 3", est_divisible(15, 3))
print("22 est divisible par 7", est_divisible(22, 7))
