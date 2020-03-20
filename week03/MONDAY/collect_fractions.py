from simplify_fraction import validate_fraction
from simplify_fraction import simplify_fraction

def validate_fractions(fractions):
	if type(fractions) == list:
		if len(fractions) > 0:
			for fraction in fractions:
				if not validate_fraction(fraction):
					return False
			return True
	return False

def find_lcm_of_numbers(numbers):
	result = max(numbers)
	is_ready = True

	while True:
		for number in numbers:
			if result % number != 0:
				is_ready = False
				break
		if is_ready:
			return result
		result += 1
		is_ready = True

def modify_nominators(nominators, denominators, lcm):
	return [int(nominators[i] * lcm / denominators[i]) for i in range(len(nominators))]

def collect_fractions(fractions):
	if validate_fractions(fractions):
		list_of_nominators = [i[0] for i in fractions]
		list_of_denominators = [i[1] for i in fractions]
		lcm = find_lcm_of_numbers(list_of_denominators)
		list_of_nominators = modify_nominators(list_of_nominators, list_of_denominators, lcm)
		return simplify_fraction(((sum(list_of_nominators), lcm)))
	else:
		raise ValueError('Invalid fractions given!')


def main():
	print(collect_fractions([(1, 4), (1, 2)]))
	print(collect_fractions([(1, 7), (2, 6)]))

if __name__ == '__main__':
	main()