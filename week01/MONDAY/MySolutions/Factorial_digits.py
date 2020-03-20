def fact_digits(n):
	list_of_digits = [int(i) for i in str(n)]
	sum_factorial = 0
	for x in list_of_digits:
		current_element = x
		current_element_factorial=1
		for y in range(1,current_element+1):
			current_element_factorial *= y
		sum_factorial+=current_element_factorial
	return sum_factorial

print(fact_digits(145))