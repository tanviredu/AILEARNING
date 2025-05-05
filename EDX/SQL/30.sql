
-- you can use subquery to 
-- eliminate duplication


/*
	WRITE A QUERY WHICH WILL FIND THE CUSTOMER
	WHO RENTED MOVIE BETWEEN
	'2005-05-25'
	AND
	'2005-05-26'
*/

SELECT
	  customer.customer_id
	, customer.first_name
	, customer.last_name
FROM
	customer
WHERE
	customer.customer_id IN (
		SELECT
			rental.customer_id
		FROM
			rental
		WHERE
			rental.rental_date
		BETWEEN
			'2005-05-25'
			AND
			'2005-05-26'
			
	)