-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.

-- SUBSTRING ( expression , start , length )

SELECT DISTINCT CITY FROM STATION 
WHERE SUBSTRING(CITY, 1, 1) NOT IN ('a', 'e', 'i', 'o', 'u') AND
SUBSTRING(CITY, LEN(CITY), 1) NOT IN ('a', 'e', 'i', 'o', 'u');