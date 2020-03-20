import unittest
from polynomial import Polynomial

class TestInitialisation(unittest.TestCase):
	def test_with_given_empty_string_should_raise_exception(self):
		string = ''

		exc = None
		try:
			polynomial = Polynomial(string)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid argument given, polynomial contains only digits from 1-9, x, +, ^')

	def test_with_given_ivalid_string_as_argument_should_raise_exception(self):
		string = '-2x^3'

		exc = None
		try:
			polynomial = Polynomial(string)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid argument given, polynomial contains only digits from 1-9, x, +, ^')

	def test_with_given_valid_string_should_create_instance(self):
		string = '3x^3+2*x^2+5*x+25'

		polynomial = Polynomial(string)

		self.assertEqual(type(polynomial), Polynomial)
		self.assertEqual(polynomial.constant, 25)
		self.assertEqual(polynomial.coefficients, [3, 2, 5])
		self.assertEqual(polynomial.powers, [3, 2, 1])
		self.assertEqual(polynomial.terms, ['3x^3', '2*x^2', '5*x'])

class TestValidateStringPolynomial(unittest.TestCase):
	def test_with_given_non_string_argument_should_return_false(self):
		string = None
		
		result = Polynomial.validate_string_polynomial(string)

		self.assertEqual(result, False)

	def test_with_given_empty_string_should_return_false(self):
		string = ''

		result = Polynomial.validate_string_polynomial(string)
		
		self.assertEqual(result, False)


	def test_with_given_string_containing_invalid_symbol_should_return_false(self):
		string = ' 20'
		
		result = Polynomial.validate_string_polynomial(string)

		self.assertEqual(result, False)

	def test_with_given_valid_string_should_return_true(self):
		string = 'x^2'
		
		result = Polynomial.validate_string_polynomial(string)

		self.assertEqual(result, True)

class TestCheckIfGivenPolynomialIsConstant(unittest.TestCase):
	def test_with_given_empty_string_should_return_false(self):
		polynomial = ''

		result = Polynomial.check_if_polynomial_is_constant(polynomial)

		self.assertEqual(result, False)

	def test_with_given_zero_as_string_should_return_false(self):
		polynomial = '0'

		result = Polynomial.check_if_polynomial_is_constant(polynomial)

		self.assertEqual(result, False)

	def test_with_given_non_digit_string_should_return_false(self):
		polynomial = 'a'

		result = Polynomial.check_if_polynomial_is_constant(polynomial)

		self.assertEqual(result, False)

	def test_with_given_one_digit_string_should_return_true(self):
		polynomial = '7'

		result = Polynomial.check_if_polynomial_is_constant(polynomial)

		self.assertEqual(result, True)

	def test_with_given_two_digit_string_with_zero_in_it_should_return_false(self):
		polynomial = '20'

		result = Polynomial.check_if_polynomial_is_constant(polynomial)

		self.assertEqual(result, False)

	def test_with_given_two_digit_string_with_non_digit_character_in_it_should_return_false(self):
		polynomial = '2a'

		result = Polynomial.check_if_polynomial_is_constant(polynomial)

		self.assertEqual(result, False)

	def test_with_given_two_digit_valid_string_should_return_true(self):
		polynomial = '29'

		result = Polynomial.check_if_polynomial_is_constant(polynomial)

		self.assertEqual(result, True)

	def test_with_given_more_than_two_digit_string_with_zero_in_it_should_return_false(self):
		polynomial = '205'

		result = Polynomial.check_if_polynomial_is_constant(polynomial)

		self.assertEqual(result, False)

	def test_with_given_more_than_two_digit_string_with_non_digit_characted_in_it_should_return_false(self):
		polynomial = '253727827a98'

		result = Polynomial.check_if_polynomial_is_constant(polynomial)

		self.assertEqual(result, False)

	def test_with_given_more_than_two_digit_valid_string_with_should_return_true(self):
		polynomial = '25372'

		result = Polynomial.check_if_polynomial_is_constant(polynomial)

		self.assertEqual(result, True)

class TestFindPolynomialTerms(unittest.TestCase):
	def test_with_given_constant_polynomial_string_should_return_list_of_one_element_constant(self):
		polynomial_string = '223'

		result = Polynomial.find_polynomial_terms(polynomial_string)

		self.assertEqual(result, [polynomial_string])

	def test_with_given_x_polynomial_string_should_return_list_of_one_element_x(self):
		polynomial_string = 'x'

		result = Polynomial.find_polynomial_terms(polynomial_string)

		self.assertEqual(result, [polynomial_string])

	def test_with_given_monomial_string_should_return_list_of_one_element_monomial(self):
		polynomial_string = '3x'

		result = Polynomial.find_polynomial_terms(polynomial_string)

		self.assertEqual(result, [polynomial_string])

	def test_with_given_binomial_string_containing_constant_should_return_list_of_two_terms_correctly(self):
		polynomial_string = '3*x+20'
		first_term = '3*x'
		second_term = '20'

		result = Polynomial.find_polynomial_terms(polynomial_string)

		self.assertEqual(result, [first_term, second_term])

	def test_with_given_binomial_string_not_containing_constant_should_return_list_of_two_terms_correctly(self):
		polynomial_string = '3*x+2x^25'
		first_term = '3*x'
		second_term = '2x^25'

		result = Polynomial.find_polynomial_terms(polynomial_string)

		self.assertEqual(result, [first_term, second_term])

	def test_with_given_trinomial_string_containing_constant_should_return_list_of_three_terms_correctly(self):
		polynomial_string = '3*x+2x^25+2'
		first_term = '3*x'
		second_term = '2x^25'
		third_term = '2'

		result = Polynomial.find_polynomial_terms(polynomial_string)

		self.assertEqual(result, [first_term, second_term, third_term])

	def test_with_given_trinomial_string_not_containing_constant_should_return_list_of_three_terms_correctly(self):
		polynomial_string = '3*x+2x^25+x^3'
		first_term = '3*x'
		second_term = '2x^25'
		third_term = 'x^3'

		result = Polynomial.find_polynomial_terms(polynomial_string)

		self.assertEqual(result, [first_term, second_term, third_term])

	def test_with_given_polynomial_string_should_return_list_of_terms_correctly(self):
		polynomial_string = 'x^4+5*x^3+3x^2+x+1'
		first_term = 'x^4'
		second_term = '5*x^3'
		third_term = '3x^2'
		fourth_term = 'x'
		fifth_term = '1'

		result = Polynomial.find_polynomial_terms(polynomial_string)

		self.assertEqual(result, [first_term, second_term, third_term, fourth_term, fifth_term])

class TestFindConstantValueInTerms(unittest.TestCase):
	def test_with_given_one_term_list_of_terms_and_term_is_constant_should_return_constant(self):
		const = '3424'
		terms = [const]

		result = Polynomial.find_constant_value_in_terms(terms)

		self.assertEqual(int(const), result)

	def test_with_given_one_term_list_of_terms_and_term_is_not_constant_should_return_0(self):
		term = '3x'
		terms = [term]

		result = Polynomial.find_constant_value_in_terms(terms)

		self.assertEqual(0, result)

	def test_with_given_two_term_list_of_terms_that_contains_constant_should_return_constant(self):
		first_term = '3x'
		constant = '22'
		terms = [first_term, constant]

		result = Polynomial.find_constant_value_in_terms(terms)

		self.assertEqual(int(constant), result)

	def test_with_given_two_term_list_of_terms_that_does_not_contain_constant_should_return_0(self):
		first_term = '3x'
		second_term = '22x^3'
		terms = [first_term, second_term]

		result = Polynomial.find_constant_value_in_terms(terms)

		self.assertEqual(0, result)

	def test_with_given_poly_term_list_of_terms_that_contains_more_than_one_constant_should_return_their_sum(self):
		first_term = '3x^2'
		second_term = '4*x'
		first_constant = '24'
		second_constant = '365'
		terms = [first_term, second_term, first_constant, second_constant]

		result = Polynomial.find_constant_value_in_terms(terms)
		expected = int(first_constant) + int(second_constant)

		self.assertEqual(expected, result)

	def test_with_given_poly_term_list_of_terms_that_does_not_contain_constant_should_return_0(self):
		first_term = '3x^5'
		second_term = '4*x^3'
		third_term = '2x^2'
		fourth_term = 'x'
		terms = [first_term, second_term, third_term, fourth_term]

		result = Polynomial.find_constant_value_in_terms(terms)

		self.assertEqual(0, result)

class TestDeleteConstantsInTerms(unittest.TestCase):
	def test_with_given_one_term_list_of_terms_and_term_is_constant_should_return_empty_list(self):
		const = '3424'
		terms = [const]

		result = Polynomial.delete_constants_in_terms(terms)
		expected = []

		self.assertEqual(expected, result)

	def test_with_given_one_term_list_of_terms_and_term_is_not_constant_should_return_same(self):
		term = '3x'
		terms = [term]

		result = Polynomial.delete_constants_in_terms(terms)

		self.assertEqual(terms, result)

	def test_with_given_two_term_list_of_terms_that_contains_constant_should_return_list_without_constant(self):
		first_term = '3x'
		constant = '22'
		terms = [first_term, constant]

		result = Polynomial.delete_constants_in_terms(terms)
		expected = [first_term]

		self.assertEqual(expected, result)

	def test_with_given_two_term_list_of_terms_that_does_not_contain_constant_should_return_same(self):
		first_term = '3x'
		second_term = '22x^3'
		terms = [first_term, second_term]

		result = Polynomial.delete_constants_in_terms(terms)

		self.assertEqual(terms, result)

	def test_with_given_poly_term_list_of_terms_that_contains_more_than_one_constant_should_return_list_without_constants(self):
		first_term = '3x^2'
		second_term = '4*x'
		first_constant = '24'
		second_constant = '365'
		terms = [first_term, second_term, first_constant, second_constant]

		result = Polynomial.delete_constants_in_terms(terms)
		expected = [first_term, second_term]

		self.assertEqual(expected, result)

	def test_with_given_poly_term_list_of_terms_that_does_not_contain_constant_should_return_same(self):
		first_term = '3x^5'
		second_term = '4*x^3'
		third_term = '2x^2'
		fourth_term = 'x'
		terms = [first_term, second_term, third_term, fourth_term]

		result = Polynomial.delete_constants_in_terms(terms)

		self.assertEqual(terms, result)

class TestFindCoefficientsOfTerms(unittest.TestCase):
	def test_with_empty_list_of_terms_should_return_empty_list(self):
		terms = []

		result = Polynomial.find_coefficients_of_terms(terms)
		expected = []

		self.assertEqual(expected, result)

	def test_with_given_one_term_list_of_terms_should_return_list_of_coefficient_before_x(self):
		term = '3x'
		terms = [term]

		result = Polynomial.find_coefficients_of_terms(terms)
		expected = [3]

		self.assertEqual(expected, result)

	def test_with_given_one_term_list_of_terms_and_no_coefficient_should_return_list_of_coefficient_1(self):
		term_one = 'x'
		term_two = 'x^2'
		terms_one = [term_one]
		terms_two = [term_two]

		result_one = Polynomial.find_coefficients_of_terms(terms_one)
		result_two = Polynomial.find_coefficients_of_terms(terms_two)
		expected = [1]

		self.assertEqual(expected, result_one)
		self.assertEqual(expected, result_two)

	def test_with_given_two_term_list_of_terms_should_return_coefficients(self):
		first_term = '3x'
		second_term = '22*x^3'
		terms = [first_term, second_term]

		result = Polynomial.find_coefficients_of_terms(terms)
		expected = [3, 22]

		self.assertEqual(expected, result)

	def test_with_given_poly_term_list_of_terms_with_all_kids_of_representation_of_term_should_return_coefficients(self):
		first_term = '3x^5'
		second_term = '4*x^3'
		third_term = '222x^2'
		fourth_term = 'x'
		terms = [first_term, second_term, third_term, fourth_term]

		result = Polynomial.find_coefficients_of_terms(terms)
		expected = [3, 4, 222, 1]

		self.assertEqual(expected, result)

class TestFindPowersOfTerms(unittest.TestCase):
	def test_with_empty_list_of_terms_should_return_empty_list(self):
		terms = []

		result = Polynomial.find_powers_of_terms(terms)
		expected = []

		self.assertEqual(expected, result)

	def test_with_given_one_term_list_of_terms_should_return_list_of_power_of_x(self):
		term = 'x^3'
		terms = [term]

		result = Polynomial.find_powers_of_terms(terms)
		expected = [3]

		self.assertEqual(expected, result)

	def test_with_given_one_term_list_of_terms_and_no_power_should_return_list_of_powers_1(self):
		term_one = 'x'
		term_two = '4x'
		terms_one = [term_one]
		terms_two = [term_two]

		result_one = Polynomial.find_powers_of_terms(terms_one)
		result_two = Polynomial.find_powers_of_terms(terms_two)
		expected = [1]

		self.assertEqual(expected, result_one)
		self.assertEqual(expected, result_two)

	def test_with_given_two_term_list_of_terms_should_return_powers(self):
		first_term = 'x^3'
		second_term = '3*x^22'
		terms = [first_term, second_term]

		result = Polynomial.find_powers_of_terms(terms)
		expected = [3, 22]

		self.assertEqual(expected, result)

	def test_with_given_poly_term_list_of_terms_with_all_kids_of_representation_of_term_should_return_powers(self):
		first_term = '3x^5'
		second_term = '4*x^27'
		third_term = '222x^2'
		fourth_term = 'x'
		terms = [first_term, second_term, third_term, fourth_term]

		result = Polynomial.find_powers_of_terms(terms)
		expected = [5, 27, 2, 1]

		self.assertEqual(expected, result)
	
class TestFindDerivative(unittest.TestCase):
	def test_with_given_constant_should_return_zero(self):
		const = '22'
		polynomial = Polynomial(const)

		result = polynomial.find_derivative()
		expected = '0'

		self.assertEqual(expected, result)

	def test_with_given_x_should_return_one(self):
		string = 'x'
		polynomial = Polynomial(string)

		result = polynomial.find_derivative()
		expected = '1'

		self.assertEqual(expected, result)

	def test_with_given_coefficient_and_x_should_return_coefficient(self):
		string_one = '33x'
		string_two = '33*x'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		expected = '33'

		self.assertEqual(expected, result_one)
		self.assertEqual(expected, result_two)

	def test_with_given_monomial_with_coefficient_and_power_two_should_return_correct_derivative(self):
		string_one = '33x^2'
		string_two = '33*x^2'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		expected = '66x'

		self.assertEqual(expected, result_one)
		self.assertEqual(expected, result_two)

	def test_with_given_monomial_with_coefficient_and_power_more_than_two_should_return_correct_derivative(self):
		string_one = '33x^4'
		string_two = '33*x^4'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		expected = '132*x^3'

		self.assertEqual(expected, result_one)
		self.assertEqual(expected, result_two)

	def test_with_given_binomial_with_terms_x_of_power_one_and_const_should_return_coefficient_before_x(self):
		string_one = 'x+24'
		string_two = '33*x+24'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		expected_one = '1'
		expected_two = '33'

		self.assertEqual(expected_one, result_one)
		self.assertEqual(expected_two, result_two)

	def test_with_given_binomial_with_terms_x_of_power_two_and_const_should_return_correct_derivative(self):
		string_one = 'x^2+24'
		string_two = '33*x^2+24'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		expected_one = '2x'
		expected_two = '66x'

		self.assertEqual(expected_one, result_one)
		self.assertEqual(expected_two, result_two)

	def test_with_given_binomial_with_terms_x_of_power_more_than_Two_and_const_should_return_correct_derivative(self):
		string_one = 'x^4+24'
		string_two = '33*x^4+24'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		expected_one = '4*x^3'
		expected_two = '132*x^3'

		self.assertEqual(expected_one, result_one)
		self.assertEqual(expected_two, result_two)

	def test_with_given_binomial_with_terms_x_of_power_one_and_x_of_power_one_should_return_correct_derivative(self):
		string_one = '22x+13x'
		string_two = 'x+x'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		expected_one = '35'
		expected_two = '2'

		self.assertEqual(expected_one, result_one)
		self.assertEqual(expected_two, result_two)

	def test_with_given_binomial_with_terms_x_of_power_two_and_x_of_power_one_should_return_correct_derivative(self):
		string_one = '22x^2+13x'
		string_two = '22*x^2+x'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		expected_one = '44x+13'
		expected_two = '44x+1'

		self.assertEqual(expected_one, result_one)
		self.assertEqual(expected_two, result_two)

	def test_with_given_binomial_with_terms_x_of_power_more_than_two_and_x_of_power_one_should_return_correct_derivative(self):
		string_one = '22x^4+13x'
		string_two = '22*x^4+x'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		expected_one = '88*x^3+13'
		expected_two = '88*x^3+1'

		self.assertEqual(expected_one, result_one)
		self.assertEqual(expected_two, result_two)

	def test_with_given_binomial_with_terms_x_of_power_two_and_x_of_power_two_should_return_correct_derivative(self):
		string_one = '22x^2+13x^2'
		string_two = '22*x^2+13*x^2'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		expected = '44x+26x'

		self.assertEqual(expected, result_one)
		self.assertEqual(expected, result_two)

	def test_with_given_binomial_with_terms_x_of_power_two_and_x_of_power_more_than_two_should_return_correct_derivative(self):
		string_one = '22x^2+13x^4'
		string_two = '22*x^2+13*x^4'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		expected = '44x+52*x^3'

		self.assertEqual(expected, result_one)
		self.assertEqual(expected, result_two)

	def test_with_given_binomial_with_terms_x_of_power_more_than_two_and_x_of_power_more_than_two_should_return_correct_derivative(self):
		string_one = '22x^4+13x^4'
		string_two = '22*x^4+13*x^4'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		expected = '88*x^3+52*x^3'

		self.assertEqual(expected, result_one)
		self.assertEqual(expected, result_two)

	def test_with_given_trinomial_should_return_correct_derivative(self):
		string_one = 'x^3+2x+1'
		string_two = '3x^2+x+54'
		string_three = '3x^3+3*x^2+2'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)
		polynomial_three = Polynomial(string_three)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		result_three = polynomial_three.find_derivative()
		expected_one = '3*x^2+2'
		expected_two = '6x+1'
		expected_three = '9*x^2+6x'

		self.assertEqual(expected_one, result_one)
		self.assertEqual(expected_two, result_two)
		self.assertEqual(expected_three, result_three)


	def test_with_given_polynomial_should_return_correct_derivative(self):
		string_one = 'x^3+x^2+2x+1'
		string_two = '3x^4+x^2+x+54'
		string_three = '3x^3+3*x^2+25*x+2'
		polynomial_one = Polynomial(string_one)
		polynomial_two = Polynomial(string_two)
		polynomial_three = Polynomial(string_three)

		result_one = polynomial_one.find_derivative()
		result_two = polynomial_two.find_derivative()
		result_three = polynomial_three.find_derivative()
		expected_one = '3*x^2+2x+2'
		expected_two = '12*x^3+2x+1'
		expected_three = '9*x^2+6x+25'

		self.assertEqual(expected_one, result_one)
		self.assertEqual(expected_two, result_two)
		self.assertEqual(expected_three, result_three)

if __name__ == '__main__':
	unittest.main()
	