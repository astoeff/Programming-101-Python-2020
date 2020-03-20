def get_prime_numbers_until_n(n):
    prime_numbers = []
    is_prime = True
    for i in range(2,n+1):
        is_prime=True
        for j in range(2,i):
            if i%j == 0:
                is_prime = False
        if is_prime == True:
            prime_numbers.append(i)
    return prime_numbers

def goldbach(n):
	prime_numbers = set(get_prime_numbers_until_n(n))
	result = []
	used_primes = set()
	for i in prime_numbers:
		if n - i in prime_numbers and i not in used_primes:
			result.append((i, n - i))
			used_primes.add(n - i)
	return result

print(goldbach(4))
print(goldbach(6))
print(goldbach(8))
print(goldbach(10))
print(goldbach(100))
