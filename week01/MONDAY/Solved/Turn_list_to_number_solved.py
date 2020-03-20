def to_number(digits):
	number_str = "".join([str(d) for d in digits])
	return int(number_str)

print(to_number([52, 23, 1]))