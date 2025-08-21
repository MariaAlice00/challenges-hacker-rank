-- Consulte o campo NAME para todas as cidades americanas na tabela CITY com populações maiores que 120.000. O CountryCode para América é USA.

SELECT NAME FROM CITY WHERE POPULATION > 120000 AND COUNTRYCODE = 'USA';