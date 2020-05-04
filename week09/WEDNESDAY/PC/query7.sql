SELECT AVG(price) as avg_price
FROM product
JOIN (SELECT * FROM pc
	  UNION ALL
	  SELECT * FROM laptop) AS subq
ON product.model = subq.model
WHERE maker = 'B'