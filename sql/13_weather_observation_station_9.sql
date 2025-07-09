-- Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

-- SUBSTRING ( expression , start , length )


SELECT DISTINCT CITY FROM STATION 
WHERE SUBSTRING(CITY, LEN(CITY), 1) NOT IN ('a', 'e', 'i', 'o', 'u');

