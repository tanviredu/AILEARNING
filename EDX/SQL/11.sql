SELECT 
	last_name, 
	COUNT(*) 
FROM actor
GROUP BY last_name
ORDER BY 2 DESC;
