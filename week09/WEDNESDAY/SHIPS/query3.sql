SELECT ship
FROM outcomes
JOIN battles ON name=battle
WHERE date LIKE "%1942%"