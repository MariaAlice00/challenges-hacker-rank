-- Consulte todas as colunas de todas as cidades americanas na tabela CITY com populações maiores que 100.000. O CountryCode para a América é USA.

SELECT * FROM CITY WHERE POPULATION > 100000 AND COUNTRYCODE = 'USA';