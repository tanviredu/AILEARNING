SELECT
	CONCAT(customer.first_name,' ',customer.last_name) 
	AS FULLNAME,
	address.phone,
	film.title,
	rental.rental_date,
	rental.return_date,
	payment.amount,
	CONCAT(staff.first_name,' ',staff.last_name) 
	AS StaffName

FROM 
	customer
INNER JOIN 
	rental
	ON 
		rental.customer_id = customer.customer_id
INNER JOIN
	inventory
	ON
		inventory.inventory_id = rental.inventory_id
INNER JOIN
	film
	ON
		film.film_id = inventory.film_id
INNER JOIN
	address
	ON
		address.address_id = customer.address_id

	
LEFT JOIN
	payment
	ON
		payment.rental_id = rental.rental_id
		
	AND
		payment.customer_id = customer.customer_id

LEFT JOIN
	staff
	ON
		staff.staff_id = payment.staff_id
WHERE  
	--customer.customer_id = 336
	--AND
	--payment.amount is null
	rental.return_date is null
ORDER BY
	rental.rental_date;
		
		