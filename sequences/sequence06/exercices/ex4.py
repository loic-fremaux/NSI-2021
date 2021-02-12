tab = [1, 2, 3, 5]
print(id(tab))
tab.insert(3, 4)
print(tab)
print(id(tab))

# La méthode semble optimisée car l'instance du tableau reste la même
