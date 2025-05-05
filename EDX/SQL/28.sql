/*
	LIST ALL THE MOVIE WHICH HAS HIGHER THAN 
	AVERAGE RENTAL RATE
*/

SELECT
	 film.title
	,film.rental_rate
FROM 
	film
WHERE 
	film.rental_rate > (
		SELECT 
			AVG(film.rental_rate)
		FROM
			film
	)
	