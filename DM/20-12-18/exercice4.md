#Exercice 4

1.
```text
FONCTION TAILLE paramètres P : Pile
VARIABLES
c : entier

DEBUT
c <- 0
Tant que non EST_VIDE(P)
    DEPILER(P)
    c <- c + 1
Fin Tant que
Retourner c
FIN
```
2.
```
FONCTION SUITE paramètres n : entier
VARIABLES
c : entier
P : Pile

DEBUT
P <- CREER_PILE()
c <- 1
Si n < 1
    Retourner erreur
Fin si
Tant que c inférieur à n + 1
    EMPILER(P, c)
    c <- c + 1
Fin Tant que
Retourner P
FIN
```
3.
```
FONCTION MOYENNE paramètres P : Pile
VARIABLES
somme : entier
elts : entier

DEBUT
somme <- 0
elts <- 0
Tant que non EST_VIDE(P)
    somme <- somme + DEPILER(P)
    elts <- elts + 1
Fin Tant que
Retourner somme / elts
FIN
```
4.
```
FONCTION BORNE paramètres P : Pile, m : entier
VARIABLES

DEBUT
Tant que non EST_VIDE(P)
    Si DEPILER(P) supérieur à m
        Retourner Faux
    Fin Si
Fin Tant que
Retourner Vrai
FIN
```