SELECT 
	actor_id,
	first_name,
	last_name 
FROM 
	actor 
WHERE first_name = 'Ben'
  AND last_name  = 'Willis'
ORDER BY 
	first_name DESC,
	last_name DESC;