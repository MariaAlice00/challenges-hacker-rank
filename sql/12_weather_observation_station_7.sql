-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

-- SUBSTRING ( expression , start , length )

SELECT DISTINCT CITY FROM STATION 
WHERE SUBSTRING(CITY, 1, 1) IN ('a', 'e', 'i', 'o', 'u') AND
SUBSTRING(CITY, LEN(CITY), 1) IN ('a', 'e', 'i', 'o', 'u');

