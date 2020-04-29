select * from classes
left join ships on classes.class = ships.class
where ships.name is NULL and ships.class in (select ships.name 
											 from ships)