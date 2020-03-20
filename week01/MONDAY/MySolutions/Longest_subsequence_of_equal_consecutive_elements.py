def group(list):
	curr_list = []
	result = []
	for x in list:
		if x in curr_list:
			pass
		else:
			if curr_list != []:
				result.append(curr_list)
			curr_list = []
		curr_list.append(x)	
	result.append(curr_list)
	return result

def max_consecutive(items):
	max_count = 0
	for x in group(items):
		if len(x) > max_count:
			max_count = len(x)
	return max_count

print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))