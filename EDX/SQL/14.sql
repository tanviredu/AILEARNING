SELECT 
	first_name,
	COUNT(*) 
FROM actor
GROUP BY first_name
HAVING COUNT(*) >3
ORDER BY first_name  ASC;
