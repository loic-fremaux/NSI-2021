# Exercice 1

## Question 1

1.

|  Pile  |
| :----: |
| 4 |
| 2 |
| 5 |
| 8 |

## Question 2
1.

```python
# noinspection PyUnresolvedReferences

def hauteur_pile(P):
    Q = creer_pile_vide()
    n = 0
    while not est_vide(P):
        n += 1
        x = depiler(P)
        empiler(Q, x)

    while not est_vide(Q):
        x = depiler(Q)
        empiler(P, x)
    return n
```

2.
```python
# noinspection PyUnresolvedReferences

def max_pile(P, i):
    Q = creer_pile_vide()
    j = 0
    c = 1
    
    x = depiler(P)
    empiler(Q, x)
    max = x
    while not est_vide(P) and c < i:
        x = depiler(P)
        empiler(Q, x)
        if x > max:
            j = c
            max = x
        c += 1

    while not est_vide(Q):
        x = depiler(Q)
        empiler(P, x)
        
    return j
```

## Question 3
```python
# noinspection PyUnresolvedReferences

def retourner(P, i):
    Q = creer_pile_vide()
    n = 0
    while not est_vide(P) and n < i:
        n += 1
        x = depiler(P)
        empiler(Q, x)
        
    R = creer_pile_vide()
    while not est_vide(Q):
        empiler(R, depiler(Q))

    while not est_vide(R):
        x = depiler(R)
        empiler(P, x)
```

## Question 4
```python
# noinspection PyUnresolvedReferences

def tri_crepes(P):
    h = hauteur_pile(P)
    c = h
    while c > 0:
        i = max_pile(P, c)
        retourner(P, i)
        retourner(P, h)

        c -= 1
```