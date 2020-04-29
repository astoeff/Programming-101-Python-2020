SELECT AVG(hd) AS avg_hd
FROM product
JOIN pc ON product.model = pc.model
WHERE maker IN (SELECT maker
				FROM product
				JOIN printer ON product.model = printer.model
				GROUP BY maker)