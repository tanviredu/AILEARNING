SELECT 
	actor_id,
	first_name,
	last_name 
FROM 
	actor 
WHERE last_name NOT LIKE 'A%'
	AND first_name NOT LIKE 'A%'

ORDER BY 
	first_name DESC,
	last_name DESC;