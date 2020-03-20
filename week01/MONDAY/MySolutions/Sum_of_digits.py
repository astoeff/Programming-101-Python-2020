def sum_of_digits(n):
	if n < 0 :
		n = abs(n)
	if n > 9 : 
		return n%10 + sum_of_digits(n//10)
	else: 
		return n
	
	 
print(sum_of_digits(-10))