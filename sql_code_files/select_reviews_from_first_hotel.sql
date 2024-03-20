-- Deliverable #6

.mode column
SELECT reviews.id, reviews.rating, reviews.text, reviews.hotel_id, reviews.customer_id 
FROM reviews
INNER JOIN hotels
ON reviews.id = reviews.hotel_id
WHERE hotels.id = 1;

