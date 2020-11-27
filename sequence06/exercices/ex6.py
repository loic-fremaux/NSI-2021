from sequence06.exercices.lists import Liste, cons

L2 = cons(5, cons(2, cons(3, cons(6, cons(1, cons(7, None))))))

# 5é élément
print(L2.cdr().cdr().cdr().cdr().car())

# 2é élément
print(L2.cdr().car())

# 1é élément
print(L2.car())
