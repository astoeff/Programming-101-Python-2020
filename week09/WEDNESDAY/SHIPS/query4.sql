SELECT country, name
FROM classes 
JOIN ships ON classes.class = ships.class
WHERE name not IN (SELECT ship
				   FROM outcomes)
GROUP BY country