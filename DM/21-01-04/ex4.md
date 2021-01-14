# Exercice 4

## Question 1
1. `num_eleve` est un identifiant unique permettant de référencer un élève à travers les différentes tables.
2. 
```SQL
INSERT INTO seconde 
(
     num_eleve,
     langue1,
     langue2,
     option,
     classe
)
VALUES
(
     '133310FE',
     'anglais',
     'espagnol',
     '',
     '2A'
);
```
NB: c'est compliqué d'insérer `133310FE` en tant qu'entier...
3.
```SQL
UPDATE seconde
SET langue2 = 'allemand'
WHERE num_eleve = '156929JJ';
```

## Question 2
1. La requête renverra tous les numéros des élèves.
2. La requête renverra le nombre total d'élèves de la table.
3. 
```SQL
SELECT COUNT(concat(langue1, langue2)) as nbr_langue_allemand
FROM seconde
WHERE langue1 = 'allemand' OR langue2 = 'allemand'
```

## Question 3
1. `num_eleve` permet de référencer facilement un élève de la table `eleve` à la table `seconde`, il établit une relation entre les deux.
2.
```SQL
SELECT nom, prenom, datenaissance
FROM eleve AS e
LEFT JOIN seconde AS s ON s.num_eleve = e.num_eleve
WHERE classe = '2A';
```

## Question 4
| coordonnees |
| :--- |
| num_eleve (clef étrangère de la table seconde, clef primaire) |
| adresse |
| code postal |
| ville |
| email |
