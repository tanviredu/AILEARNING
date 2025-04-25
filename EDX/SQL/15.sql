SELECT 
	first_name,
	COUNT(*) 
FROM actor
GROUP BY first_name
HAVING COUNT(*) BETWEEN 3 AND 4
ORDER BY first_name  ASC;
