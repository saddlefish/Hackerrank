--Query a count of the number of cities in CITY having a Population larger than 100,000--

select DISTINCT count(NAME)
from CITY
WHERE POPULATION > 100000;
