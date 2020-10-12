import itertools

voyelles = list("aeiouy")
letters = "algorithme"

count = 0

for l in itertools.permutations(list(letters)):
    if l[0] in voyelles and l[-1] not in voyelles:
        count += 1

print(count)
