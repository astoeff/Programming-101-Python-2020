def palindrome(n):
	list_of_symbols = [i for i in str(n)]
	symbol_to_check_posiiton=-1
	for x in list_of_symbols:
		if x == list_of_symbols[symbol_to_check_posiiton]:
			symbol_to_check_posiiton-=1
		else:
			return False
	return True

print(palindrome("baba"))