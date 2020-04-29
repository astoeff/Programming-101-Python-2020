SELECT AVG(price)
FROM product
JOIN pc ON product.model = pc.model
WHERE maker = 'A'