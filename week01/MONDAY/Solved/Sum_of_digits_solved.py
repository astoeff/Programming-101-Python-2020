def sum_of_digits(n):
	n_str=str(n)
	if n_str[0] == '-':
		n_str = n_str[1::]
	return sum([int(i) for i in n_str])

print(sum_of_digits(-245))