--2-fans.sql
--ordered by fans all around.

SELECT origin AS origin, SUM(fans) AS nb_fans
FROM  metal_bands
WHERE origin IS NOT NULL AND fans IS NOT NULL
GROUP BY origin
ORDER BY nb_fans DESC;
ORDER BY nb_fans DESC;