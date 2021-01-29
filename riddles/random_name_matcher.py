from random import randint

group_size = 5

names = [
    "Tom",
    "Loïc",
    "Nathan",
    "Oscar",
    "Samuel",
    "Lilian",
    "Clément",
    "Maxime",
    "Antoine",
    "Noé",
    "Maxence",
    "The Boss"
]

themes = ["POO", "SQL", "récursivité", "tris", "HTML/CSS", "Javascript", "Programmation fonctionnelle",
          "Structure d'arbre", "Structure linéaire", "Architecture des ordinateurs", "Réseaux", "Langage python"]

matched = []
first_len = len(names)
while (tomtom := len(names)) > group_size - (first_len % group_size) - 1:
    c = 0
    group = []
    while c < group_size:
        c += 1
        fi = randint(0, tomtom - c)
        m = names[fi]
        names.pop(fi)
        ft = randint(0, len(themes) - 1)
        theme = themes[ft]
        themes.pop(ft)

        group.append((m, theme))

    matched.append(group)

if len(names) > 0:
    print(names, " is alone")

for tomtom in matched:
    print(tomtom)
