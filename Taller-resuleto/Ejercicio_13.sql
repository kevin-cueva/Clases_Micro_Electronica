/*Consulte el campo NOMBRE para todas las ciudades estadounidenses en la tabla CITY con
 poblaciones superiores a 120000. El código de país para América es EE. UU.

La tabla CITY se describe de la siguiente manera:*/

SELECT Name from CITY
where Population>120000 and CountryCode = 'USA';