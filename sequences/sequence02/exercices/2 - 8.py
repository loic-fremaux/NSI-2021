def recherche5(motif, text):
    lMotif = len(motif) - 1
    lText = len(text) - 1
    matching = lMotif
    for i in range(len(text)):
        if text[lText - i] == motif[matching]:
            matching -= 1
        else:
            matching = lMotif
        if matching == 0:
            return True
    return False


#  TESTS
print(recherche5("log", "zoologielog"))
print(recherche5("logique", "zoologielog"))
