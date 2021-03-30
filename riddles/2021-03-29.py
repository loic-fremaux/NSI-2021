recettes = {
    "quatre-quart": {"oeuf": 4, "beurre": 250, "sucre": 250, "farine": 250},
    "fondant chocolat": {"oeuf": 3, "beurre": 100, "sucre": 100, "farine": 50, "chocolat": 200},
    "moelleux chocolat": {"oeuf": 4, "beurre": 125, "sucre": 150, "farine": 125, "chocolat": 200},
    "brownies chocolat": {"oeuf": 4, "beurre": 150, "sucre": 125, "farine": 80, "chocolat": 350},
    "cookies chocolat": {"oeuf": 2, "beurre": 250, "sucre": 250, "farine": 350, "chocolat": 300},
    "petits sables de noel": {"oeuf": 2, "beurre": 125, "sucre": 125, "farine": 300, "amande": 125},
    "financiers": {"oeuf": 4, "beurre": 100, "sucre": 150, "farine": 35, "amande": 75}
}

ingredients = {"oeuf": 10, "beurre": 600, "sucre": 800, "farine": 1000, "amande": 800, "chocolat": 800}


def gateau_faisable(gateau, ingredient):
    gateau = recettes[gateau]
    for value in gateau:
        if gateau[value] > ingredient[value]:
            return False
    return True


print(gateau_faisable("quatre-quart", ingredients))
print(gateau_faisable("fondant chocolat", ingredients))
print(gateau_faisable("moelleux chocolat", ingredients))
print(gateau_faisable("brownies chocolat", ingredients))
print(gateau_faisable("cookies chocolat", ingredients))
