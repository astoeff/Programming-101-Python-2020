def nan_expand(times):
	empty = '\"\"'
	once = 'Not a NaN'
	more = 'Not a '
	result = ''
	if times == 0:
		return empty
	elif times == 1:
		return once
	else:
		for x in range(1,times):
			result += more
		result += once
	return result

print(nan_expand(0))
print(nan_expand(1))
print(nan_expand(2))
print(nan_expand(3))