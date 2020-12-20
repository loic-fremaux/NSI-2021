# Exercice 1
1. La clé secondaire `idSpectacle` de `Programmation` fait référence à la clé primaire `idSpectacle` de `Spectacle`
2. La clé primaire de `Programmation` est constituée de 2 attributs car on ne peut pas avoir 2 spectacles au même endroit et à la même date
3.
```SQL
SELECT titreSpectacle FROM Spectacle;
```
4.
```SQL
SELECT * FROM Lieu WHERE superficie > 10;
```
5.
```SQL
SELECT * FROM Lieu WHERE adresse LIKE '%amiens%';
```
6.
```SQL
SELECT a.nom, s.titreSpectacle
FROM Artiste as a
LEFT JOIN Spectacle as s ON s.idSpectacle = a.idSpectacle;
```
7.
```SQL
SELECT s.titreSpectacle, l.adresse, p.tarif
FROM Spectacle as s
WHERE p.date = '25/03/2021'
LEFT JOIN Programmation as p ON p.idSpectacle = s.idSpectacle
LEFT JOIN Lieu as l ON l.idLieu = s.idLieu;
```
8.
```SQL
SELECT COUNT(a.idArtiste)
FROM Spectacle as s
WHERE s.idSpectacle = 20
LEFT JOIN Artiste as a ON a.idSpectacle = s.idSpectacle;
```
9.
```SQL
SELECT p.date, s.titreSpectacle
FROM Spectacle as s
WHERE p.tarif < 20 
LEFT JOIN Programmation as p ON p.idSpectacle = s.idSpectacle;
```
