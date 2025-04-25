SELECT 
	last_name,
	first_name,
	COUNT(*) 
FROM actor
GROUP BY last_name,first_name
HAVING COUNT(*) >1
ORDER BY 3 DESC;
