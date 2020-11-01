








def algo():
    P = 10500
    n = 2002
    while P > 1500:
        P = P - 0.14 * P
        n = n + 1
    return n









print(algo())
