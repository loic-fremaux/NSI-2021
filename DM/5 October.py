def nb_caract(lettre, mot):
    c = 0
    for l in mot:
        if l == lettre:
            c += 1
    return c


# TESTS
print(nb_caract('i', 'informatique'))
print(nb_caract('o', 'zoologie'))


def max_caract(mot):
    tab = {}
    for l in mot:
        if l in tab:
            tab[l] += 1
        else:
            tab[l] = 1

    high = mot[0]
    for k, v in tab.items():
        if v > tab[high]:
            high = k

    return high


# TESTS
print(max_caract("ananas"))


def max_caract_improved(mot):
    tab = {}
    for l in mot:
        if l in tab:
            tab[l] += 1
        else:
            tab[l] = 1

    high = max(tab.values())
    for k, v in list(tab.items()):
        if v < high:
            tab.pop(k)

    return tab


# TESTS
print(max_caract_improved("mississipi"))


def recherche(motif, mot):
    matching = 0
    lMotif = len(motif)
    for i in range(len(mot)):
        if mot[i] == motif[matching]:
            matching += 1
        else:
            matching = 0
        if matching == lMotif:
            return True
    return False


# TESTS
print(recherche("log", "zoologie"))
print(recherche("logique", "zoologie"))
