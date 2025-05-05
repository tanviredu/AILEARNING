/*
	IF THERE IS A AGGRAGATIOJN 
	THERE WILL BE A GROUP BY
	AND YOU CAN AVOID USING DISTINCT
	USING GROUP BY
*/


SELECT 
	   customer.customer_id
	,  CONCAT(customer.first_name, ' ', customer.last_name)
	,  COUNT(*) AS "Count Of Rentals"
	,  SUM (payment.amount) AS "Total Amount spent"
	,  ROUND (AVG (film.length),2) AS "AVG Length Of Movie (rounded)"
	,  TRUNC (AVG (film.length),2) AS "AVG Length Of Movie (Truncated)"
	,  ROUND (AVG (film.length)) AS "AVG Length Of Movie (rounded Whole)"
	,  TRUNC (AVG (film.length)) AS "AVG Length Of Movie (Truncated Whole)"
	,  MIN (rental.rental_date) AS "Earlient Rental Date"
	,  MAX (rental.rental_date) AS "Last Rental date"

FROM
	film
INNER JOIN
	inventory
ON
	inventory.film_id = film.film_id
INNER JOIN
	rental
ON
	rental.inventory_id = inventory.inventory_id
INNER JOIN
	customer
ON
	customer.customer_id = rental.customer_id
LEFT JOIN
	payment
ON
	payment.rental_id = rental.rental_id
AND
	payment.customer_id = customer.customer_id
	
GROUP BY
	customer.customer_id

ORDER BY
	3 DESC
	