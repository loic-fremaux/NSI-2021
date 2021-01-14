# Exercice 2

# Question 1
1. 255
2. 255

# Question 2
1. r = 13
2. q = 4

# Question 3

```python
signes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


def bTodec(mot, b):
    assert 1 < b < 17
    assert type(mot) == str
    result = 0
    p = len(mot)
    for i in range(p):
        result = result + signes.index(mot[p - i - 1]) * b ** i
    return result
```

# Question 4
1. La fonction récursive doit s'arrêter lorsque la chaine de caractères est vide
2. 
```python
signes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

def b_rec(mot, b):
    assert 1 < b < 17
    assert type(mot) == str

    if len(mot) == 0:
        return 0

    p = len(mot) - 1
    return (signes.index(mot[p]) * b ** p) + b_rec(mot[1:], b)
```