def is_iterable(iterable):
	if type(iterable) == list:
		return 'list' 
	elif type(iterable) == tuple:
		return 'tuple'
	return 'invalid type'	

def check_if_iterable_is_homogene(iterable):
	it_type = None
	for i in iterable:
		if it_type == None:
			it_type = type(i)
		else:
			if type(i) != it_type:
				return False
	return True

def check_is_list_of_dictionaries_given(given_list):
	for i in given_list:
		if type(i) != dict:
			return False
	return True

def check_if_key_is_in_all_dictionaries_in_iterable(iterable, key):
	for dictionary in iterable:
		if key not in dictionary:
			return False
	return True

def sort_dictionary(dictionary, ascending, key):
	for i in range(len(dictionary)):
		for j in range(i,len(dictionary)):
			if ascending == True:
				if dictionary[i][key] > dictionary[j][key]:
					left =  dictionary[j]
					dictionary[j] = dictionary[i]
					dictionary[i] = left
			else:
				if dictionary[i][key] < dictionary[j][key]:
					left =  dictionary[j]
					dictionary[j] = dictionary[i]
					dictionary[i] = left

	return dictionary


def my_sort(iterable = None, ascending = True, key = None):
	if iterable == None:
		return []

	is_tuple = False
	is_dict = False
	if is_iterable(iterable) == 'tuple':
		is_tuple = True
	elif is_iterable(iterable) == 'list':
		pass
	else:
		raise ValueError('Invalid iterable given!')

	if not check_if_iterable_is_homogene(iterable):
		raise ValueError('Iterable is not homogene!')

	iterable = list(iterable)

	if check_is_list_of_dictionaries_given(iterable):	
		if key == None:
			pass
		else:
			if type(key) != str:
				raise ValueError('Key {k}: not a string!'.format(k = key))
			if not check_if_key_is_in_all_dictionaries_in_iterable(iterable, key):
				raise ValueError('Key {k} not in all dictionaries!'.format(k = key))
		
			iterable = sort_dictionary(iterable, ascending, key)
		
		is_dict = True


	if is_dict == False:
		for i in range(len(iterable)):
			for j in range(i,len(iterable)):
				if ascending == True:
					if iterable[i] > iterable[j]:
						left =  iterable[j]
						iterable[j] = iterable[i]
						iterable[i] = left
				else:
					if iterable[i] < iterable[j]:
						left =  iterable[j]
						iterable[j] = iterable[i]
						iterable[i] = left
	if is_tuple == True:
		return tuple(iterable)

	return iterable

def main():
	pass

if __name__ == '__main__':
	main()