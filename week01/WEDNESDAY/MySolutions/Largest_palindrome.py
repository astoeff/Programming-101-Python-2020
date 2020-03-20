def is_string_palindrome(string):
	return string == string[::-1]

def get_largest_palindrome(n):
	for i in range(n-1,1,-1):
		str_i = str(i)
		if is_string_palindrome(str_i):
			return i
	return 1

print(get_largest_palindrome(99))
print(get_largest_palindrome(252))
print(get_largest_palindrome(994687))
print(get_largest_palindrome(754649))