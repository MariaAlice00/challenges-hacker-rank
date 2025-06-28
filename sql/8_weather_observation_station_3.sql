-- Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.

-- ID PAR, EXCLUIR DUPLICATAS

-- MOD(ID, 2) = 0; quando o resto da divisão do ID e 2 é 0
-- DISTINCT - linhas exclusivas

SELECT DISTINCT CITY FROM STATION 
WHERE MOD(ID, 2) = 0;