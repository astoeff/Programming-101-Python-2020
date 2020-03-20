def gas_stations(distance, tank_size, stations):
    travelled_distance = 0
    fuel_used = 0
    fuel_left = 90
    result = []
    for i in stations:
    	# print(travelled_distance)
    	# print(fuel_used)
    	# print(fuel_left)
    	if travelled_distance + fuel_left > i:
    		fuel_used = i
    	else:
    		result.append(travelled_distance)
    		fuel_used = i - travelled_distance
    	fuel_left = 90 - fuel_used
    	travelled_distance = i
    if travelled_distance + fuel_left < distance:
    	result.append(travelled_distance)
    return result

print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))