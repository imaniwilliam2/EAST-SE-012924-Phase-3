.mode column

SELECT customers.*
FROM customers
INNER JOIN reviews ON customer_id = reviews.customer_id
WHERE reviews.hotel_id = 1
GROUP BY customers.id;
