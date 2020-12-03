from sequence06.exercices.files import File

F1 = File()\
    .enfiler(3)\
    .enfiler(1)\
    .enfiler(5)\
    .enfiler(6)\
    .enfiler(4)\
    .enfiler(2)

print(F1.defiler())
print(F1.defiler())

F1.defiler()
F1.defiler()

print(F1.defiler())
