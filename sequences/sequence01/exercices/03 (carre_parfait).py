def carre_parfait(n):
    """
    check if a number is a perfect square
    :param n: the number to check
    :return: True if a number is a perfect square or else False
    """
    return (n ** 0.5) % 1 == 0


print(carre_parfait(25))
print(carre_parfait(66))
