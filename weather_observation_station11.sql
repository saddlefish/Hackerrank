/*
Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
*/

SELECT DISTINCT CITY
FROM STATION
WHERE NOT (CITY LIKE 'a%' or
       CITY LIKE 'e%' or
       CITY LIKE 'i%' or
       CITY LIKE 'o%' or
       CITY LIKE 'u%')
       OR NOT
      (CITY LIKE '%a' or
       CITY LIKE '%e' or
       CITY LIKE '%i' or
       CITY LIKE '%o' or
       CITY LIKE '%u')
