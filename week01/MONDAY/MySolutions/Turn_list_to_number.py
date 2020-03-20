import math

def number_of_digits(n):
	if n > 0:
		return int(math.log10(n)) + 1
	elif n == 0:
		return 1
	else:
		return int(math.log10(-n)) + 1

def to_number(digits):
	pow = 0
	list_of_digits_length=len(digits)
	x_range = range(list_of_digits_length)
	result = 0
	for x in x_range:
		print("x is ")
		print(x)
		print(result)
		curr_element=(digits[-(x+1)]*(10**pow))
		print(curr_element)
		result+=curr_element
		pow+=number_of_digits(curr_element)
	return result

print(to_number([52, 23, 1]))