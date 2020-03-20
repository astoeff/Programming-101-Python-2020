from collect_fractions import validate_fractions
from simplify_fraction import simplify_fraction

def sort_fractions(fractions, ascending = True):
	if validate_fractions(fractions):
		if type(ascending) == bool:
			return sorted(fractions, key = lambda c: c[0]/c[1], reverse = not ascending)
		else:
			raise ValueError('Invalid order given, needs to be bool!')
	else:
		raise ValueError('Invalid fractions given!')

def main():
	print(sort_fractions([(2, 3), (1, 2)]))
	print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
	print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))

if __name__ == '__main__':
	main()