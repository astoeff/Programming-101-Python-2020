def sum_of_digits(n):
	return sum([int(i) for i in (str(n)[1::] if str(n)[0] == '-' else str(n))])

print(sum_of_digits(-245))