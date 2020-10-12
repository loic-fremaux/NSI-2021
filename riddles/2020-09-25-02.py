def child_numbers(n):
    result = [[] for i in range(n + 1)]
    for i in range(1, n + 1):
        result[i].append(str(i))
        for j in range(1, i):
            for nb in result[i - j]:
                result[i].append(str(j) + nb)

    return result[n]


def parent(nb):
    nbStr = str(nb)
    unit = nbStr[1]
    rest = nbStr[0]
    result = child_numbers(int(rest))
    for i in range(0, len(result)):
        result[i] = result[i] + unit
    return result


print(parent(31))
