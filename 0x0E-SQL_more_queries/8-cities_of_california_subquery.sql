-- Script that lists all the cities of California registered in the database

-- Query to list all the cities from California

SELECT id, name
FROM cities

--Query to get the id of Califonia
WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = "California");
