SELECT name, country, numguns, launched 
FROM classes
JOIN ships ON classes.class = ships.class
