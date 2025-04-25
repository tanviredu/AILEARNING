SELECT 
	CONCAT(A.first_name,' ',A.last_name) AS FullName,F.title
FROM
	actor AS A
LEFT OUTER JOIN
	film_actor AS FA
	ON FA.actor_id = A.actor_id
LEFT OUTER JOIN 
	film AS F
	ON F.film_id = FA.film_id
WHERE
	A.first_name = 'Woody'
AND 
	A.last_name = 'Hoffman'
ORDER BY
	F.title ASC;