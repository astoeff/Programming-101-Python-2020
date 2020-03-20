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


def prime_factorization(n):
    prime_numbers = get_prime_numbers_until_n(n)
    all_primes_map = {}
    result = {}
    final = []
    for i in prime_numbers:
        all_primes_map[i]=0
    while n > 1:
        for x in prime_numbers:
            if n%x == 0:
                all_primes_map[x] += 1
                n/=x
    for x in prime_numbers:
        if all_primes_map[x] == 0:
            pass
        else:
            result[x] = all_primes_map[x]
    for x in result:
        current_el = []
        current_el.append(x)
        current_el.append(result[x])
        final.append(current_el)
    final.sort()
    return final

print(prime_factorization(10))
print(prime_factorization(14))
print(prime_factorization(356))
print(prime_factorization(89))
print(prime_factorization(1000))