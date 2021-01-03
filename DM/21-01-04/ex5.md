# Exercice 5

## Question 1
1. A -> C -> F -> G
2. Table de routage du routeur G

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| A | F | 3 |
| B | E | 3 |
| C | F | 2 |
| D | E | 2 |
| E | E | 1 |
| F | F | 1 |

## Question 2
Table de routage du routeur A

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| B | B | 1 |
| D | D | 1 |
| E | D | 2 |
| F | D | 4 |
| G | D | 3 |

## Question 3
1. 10⁸÷(10×10⁹) = 0.01
2. 10⁸÷5÷10⁹ = 0.02 donc 0.02Gb/s soit 0.02 * 1000 = 20Mb/s

## Question 4
Chemins possibles pour aller de A à G

Formule utilisée : **`10⁸÷(x×10⁹)`** où x = débit en Gb/s

| Liaison | Coût |
| :----: | :---: |
| A -> B | 0.01 |
| A -> D | 0.01 |
| A -> C | 10 |
| B -> D | 5 |
| C -> F | 1 |
| C -> E | 2 |
| D -> E | 0.001 |
| E -> G | 1 |
| F -> G | 1 |

| Chemin | Coûts |
| :----: | :---: |
| A -> B -> D -> E -> G | 6.011 |
| A -> B -> D -> E -> C -> F -> G | 9.011 |
| **A -> D -> E -> G** | **1.01** |
| A -> D -> E -> C -> F -> G | 4.011 |
| A -> C -> F -> G | 13 |
| A -> C -> E -> G | 12 |

Le meilleur trajet selon le protocole OSPF est donc **A -> D -> E -> G**