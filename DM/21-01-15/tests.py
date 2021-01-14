signes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


def bTodec(mot, b):
    assert 1 < b < 17
    assert type(mot) == str
    result = 0
    p = len(mot)
    for i in range(p):
        result = result + signes.index(mot[p - i - 1]) * b ** i
    return result


def b_rec(mot, b):
    assert 1 < b < 17
    assert type(mot) == str

    if len(mot) == 0:
        return 0

    p = len(mot) - 1
    return (signes.index(mot[p]) * b ** p) + b_rec(mot[1:], b)


print(b_rec('1111', 2))
