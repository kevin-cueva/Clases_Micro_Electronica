/*Consulte todas las columnas de todas las ciudades estadounidenses en la tabla CITY con poblaciones
superiores a 100000. El código de país para América es EE. UU.

La tabla CITY se describe de la siguiente manera:

https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true
*/

SELECT * FROM CITY
WHERE Population>100000 and CountryCode = 'USA'