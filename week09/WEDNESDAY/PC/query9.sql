SELECT maker, MAX(price)
FROM product
JOIN pc ON product.model = pc.model