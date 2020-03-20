import re

class Polynomial:
	def validate_string_polynomial(polynomial):
		if type(polynomial) != str or polynomial == '':
			return False
		else:
			allowed_symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '+', 'x', '^', '*']
			for symbol in polynomial:
				if symbol not in allowed_symbols:
					return False
			return True

	def check_if_polynomial_is_constant(polynomial):
		regex = '^[1-9]+$'

		if bool(re.match(regex, polynomial)):
			return True
		return False

	def find_polynomial_terms(polynomial):
		return polynomial.split('+')

	def find_constant_value_in_terms(terms):
		constant = 0
		for term in terms:
			if Polynomial.check_if_polynomial_is_constant(term):
				constant += int(term)
		return constant

	def delete_constants_in_terms(terms):
		terms_without_constants = []
		for term in terms:
			if not Polynomial.check_if_polynomial_is_constant(term):
				terms_without_constants.append(term)			
		return terms_without_constants

	def find_coefficients_of_terms(terms):
		coefficients = []
		for term in terms:
			term_parts = term.split('x')
			if term_parts[0] == '':
				coefficients.append(1)
			else:
				if '*' in term:
					coefficients.append(int(term_parts[0][:len(term_parts[0])-1]))
				else:
					coefficients.append(int(term_parts[0]))
		return coefficients

	def find_powers_of_terms(terms):
		powers = []
		for term in terms:
			term_parts = term.split('x')
			if term_parts[1] == '':
				powers.append(1)
			else:
				powers.append(int(term_parts[1][1:]))
		return powers

	def find_derivative(self):
		derivative = ''
		for i in range(len(self.coefficients)):
			coefficient = self.coefficients[i]*self.powers[i]
			power = self.powers[i] - 1
			if coefficient == 1 and power + 1 == 1:
				derivative += '1'
			else:
				if coefficient != 1:
					derivative += str(coefficient)
				if power != 0:
					if power != 1:
						derivative += '*'
						derivative += 'x'
						derivative += '^'
						derivative += str(power)
					else:
						derivative += 'x'
			derivative += '+'
		if derivative == '':
			return '0'		
		if 'x' not in derivative:
			result = derivative.split('+')
			result = list(filter(('').__ne__, result))
			return str(sum([int(i) for i in result]))

		return derivative[:len(derivative)-1]

	def __init__(self, polynomial):
		if not Polynomial.validate_string_polynomial(polynomial):
			raise ValueError('Invalid argument given, polynomial contains only digits from 1-9, x, +, ^')
		terms = Polynomial.find_polynomial_terms(polynomial)
		self.constant = Polynomial.find_constant_value_in_terms(terms) 
		self.terms = Polynomial.delete_constants_in_terms(terms)
		self.coefficients = Polynomial.find_coefficients_of_terms(self.terms)
		self.powers = Polynomial.find_powers_of_terms(self.terms)

if __name__ == '__main__':		
	pol = Polynomial("x")
	print(pol.__dict__)
		

	str_1 = '2*x^3+x'
	str_2 = '1'
	str_3 = 'x^4+11*x^3'
	str_4 = '1+x^2'
	str_5 = '3x^2'
	str_6 = '2x^3+3x+1'

	pol_1 = Polynomial(str_1)
	pol_2 = Polynomial(str_2)
	pol_3 = Polynomial(str_3)
	pol_4 = Polynomial(str_4)
	pol_5 = Polynomial(str_5)
	pol_6 = Polynomial(str_6)

	print(pol_1.find_derivative())
	print(pol_2.find_derivative())
	print(pol_3.find_derivative())
	print(pol_4.find_derivative())
	print(pol_5.find_derivative())
	print(pol_6.find_derivative())
# list_1 = str_1.split('+')
# list_2 = str_2.split('+')
# list_3 = str_3.split('+')
# list_4 = str_4.split('+')
# list_5 = str_5.split('+')
# list_6 = str_6.split('+')

# for i in list_1:
# 	print(i.split('x'))
# print('--------------------')
# for i in list_2:
# 	print(i.split('x'))
# print('--------------------')
# for i in list_3:
# 	print(i.split('x'))
# print('--------------------')	
# for i in list_4:
# 	print(i.split('x'))
# print('--------------------')	
# for i in list_5:
# 	print(i.split('x'))
# print('--------------------')	
# for i in list_6:
# 	print(i.split('x'))


# print(list_1)
# print(list_2)
# print(list_3)
# print(list_4)
# print(list_5)

