SELECT 
	last_name,
	first_name,
	CONCAT(first_name,' ',last_name) AS FullName,
	CONCAT(last_name,',',first_name) AS FullName
FROM 
	actor;