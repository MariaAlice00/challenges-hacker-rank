-- Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

-- cidade com nome mais curto e mais longo
-- se houver mais de uma cidade com a mesma quantidade de letras, escolher a primeira em ordem alfabética

SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY), CITY LIMIT 1;

SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY) DESC, CITY LIMIT 1;

-- SELECT CITY, LENGTH(CITY): seleciona o nome da cidade e calcula o número de caracteres de cada nome 
-- ORDER BY LENGTH(CITY), CITY: ordenar pelo número de caracteres em ordem crescente e em ordem alfabética (sem houver mais de uma cidade com o mesmo número de caracteres);
-- LIMIT 1: pega apenas a primeira linha