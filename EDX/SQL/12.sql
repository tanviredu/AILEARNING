SELECT 
	last_name,
	first_name,
	COUNT(*) 
FROM actor
GROUP BY last_name,first_name
ORDER BY 3 DESC;
