SELECT 
	last_name,
	first_name
FROM 
	actor 
WHERE last_name <= 'Allen' 
	AND first_name <> 'Kim'

ORDER BY 
last_name,
first_name