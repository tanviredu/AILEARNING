-- find actors of the  the movie "Snowman Rollercoaster"

SELECT 
	CONCAT(A.first_name,' ',A.last_name) 
	AS 
		Fullname,
	F.title
FROM
	actor as A

INNER JOIN 
	film_actor AS FA
	ON 
		FA.actor_id = A.actor_id
INNER JOIN
	film AS F
	ON
		F.film_id = FA.film_id

WHERE 
	F.title = 'Snowman Rollercoaster'
ORDER BY F.title;



