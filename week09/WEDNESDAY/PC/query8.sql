SELECT *
FROM (SELECT maker, COUNT(pc.model) as count
	  FROM product
	  JOIN pc ON product.model = pc.model
	  GROUP BY maker)
WHERE count >= 3