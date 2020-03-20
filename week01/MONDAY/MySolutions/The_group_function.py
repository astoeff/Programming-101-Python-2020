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
	#previous=list[0]
	#sequence=[previous]
	#result=[]
	#for x in list:
	#	current = x
	#	if previous == current & previous != list[0]:
	#		sequence.append(current)
	#	else:
	#		result.append(sequence)
	#		sequence = []
	#	previous=current
	#return result

print(group([1, 1, 1, 2, 3, 1, 1]))
print(group([1, 2, 1, 2, 3, 3]))