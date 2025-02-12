SELECT p.name, p.description, p.price, p.stock_quantity 
FROM products p
JOIN brands b ON p.brand_id = b.id
WHERE b.name = 'Apple';