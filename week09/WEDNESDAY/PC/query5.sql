SELECT speed, AVG(price)
FROM pc
WHERE speed > 500
GROUP BY speed