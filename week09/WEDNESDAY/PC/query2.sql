SELECT product.maker, AVG(SCREEN)
FROM product 
JOIN laptop ON product.model = laptop.model
GROUP BY product.maker