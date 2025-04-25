SELECT 
	last_name,
	first_name
FROM
	actor
WHERE
	last_name 
	BETWEEN 'A' AND 'B'
ORDER BY
	last_name,first_name;