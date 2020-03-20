import math

def to_digits(n):	
	n = abs(n)	
	return [int(i) for i in str(n)]
	
print(to_digits(15357))
print(to_digits(99999))
print(to_digits(123023))
print(to_digits(-20))