-- Query the average population for all cities in CITY, rounded down to the nearest integer.

SELECT Round(AVG(POPULATION), 0)
FROM CITY;
