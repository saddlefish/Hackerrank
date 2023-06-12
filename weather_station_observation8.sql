/*
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
*/

SELECT CITY
FROM STATION
WHERE (CITY LIKE 'a%' or
       CITY LIKE 'e%' or
       CITY LIKE 'i%' or
       CITY LIKE 'o%' or
       CITY LIKE 'u%')
       AND
      (CITY LIKE '%a' or
       CITY LIKE '%e' or
       CITY LIKE '%i' or
       CITY LIKE '%o' or
       CITY LIKE '%u')
