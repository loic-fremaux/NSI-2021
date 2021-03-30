from itertools import combinations_with_replacement

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


def gateaux_faisables(gateaux, ingredient):
    ingredients_conso = {}
    for gateau in gateaux:
        gateau = recettes[gateau]
        for ingr in gateau:
            if ingr not in ingredients_conso.keys():
                ingredients_conso[ingr] = 0
            if gateau[ingr] > ingredient[ingr] - ingredients_conso[ingr]:
                return False
            else:
                ingredients_conso[ingr] += gateau[ingr]

    for ingr in ingredients_conso.keys():
        ingredient[ingr] -= ingredients_conso[ingr]

    return True

r = {}
high = 0
for i in range(len(ingredients)):
    r[i] = []
    p = combinations_with_replacement(recettes.keys(), i)
    for a in list(p):
        if gateaux_faisables(list(a), ingredients.copy()):
            high = i
            r[i].append(list(a))

print(high)
for v in r[high]:
    print(v)
