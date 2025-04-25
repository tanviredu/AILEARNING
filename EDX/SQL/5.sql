SELECT 
	actor_id,
	first_name,
	last_name 
FROM 
	actor 
WHERE last_name LIKE 'H%s'

ORDER BY 
	first_name DESC,
	last_name DESC;