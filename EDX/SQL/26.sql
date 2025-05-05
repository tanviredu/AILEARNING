SELECT
	*
FROM
	film
JOIN
	inventory
ON film.film_id = inventory.film_id;