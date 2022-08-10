-- list all cities in carlifornia and orders by ID
SELECT id, name FROM cities WHERE state_id IN (
	SELECT id FROM states WHERE name = "California"
);
ORDER BY id;
