/*
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. 
The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

Note: Print NULL when there are no more names corresponding to an occupation.
*/

SELECT MIN(IF(OCCUPATION = 'Doctor', NAME, NULL)), MIN(IF(OCCUPATION = 'Professor', NAME, NULL)), MIN(IF(OCCUPATION = 'Singer', NAME, NULL)), MIN(IF(OCCUPATION = 'Actor', NAME, NULL))
FROM (
    SELECT ROW_NUMBER() OVER(PARTITION BY OCCUPATION ORDER BY NAME) AS row_num,
        NAME,
        OCCUPATION
    FROM OCCUPATIONS
) AS new
GROUP BY row_num
