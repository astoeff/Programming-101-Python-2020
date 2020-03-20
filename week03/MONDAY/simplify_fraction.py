def validate_fraction(fraction):
	if type(fraction) == tuple:
		if len(fraction) == 2:
			if type(fraction[0]) == int and type(fraction[1]) == int:
				if fraction[1] != 0:
					return True
	return False

def find_dividers_of_number(number):
	dividers = set()
	for n in range(2, number + 1):
		if number % n == 0:
			dividers.add(n)

	return dividers

def simplify_fraction(fraction):
	if validate_fraction(fraction):
		nominator = fraction[0]
		denominator = fraction[1]
		nominator_dividers = find_dividers_of_number(nominator)
		denominator_dividers = find_dividers_of_number(denominator)
		nominator_and_denominator_dividers = nominator_dividers & denominator_dividers
		for i in sorted(list(nominator_and_denominator_dividers), reverse = True):
			if nominator % i == 0 and denominator % i == 0:
				nominator /= i
				denominator /= i

		return (int(nominator), int(denominator))

	raise ValueError('Invalid fraction given!')



def main():
	pass

if __name__ == '__main__':
	main()