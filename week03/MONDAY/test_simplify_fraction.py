import unittest
from simplify_fraction import simplify_fraction
from simplify_fraction import validate_fraction
from simplify_fraction import find_dividers_of_number

class TestValidateFraction(unittest.TestCase):

	def test_with_given_non_tuple_fraction_should_return_false(self):
		fraction = None

		result = validate_fraction(fraction)

		self.assertEqual(result, False)

	def test_with_given_tuple_with_not_two_elements_should_return_false(self):
		fraction = (1, 3, 5)

		result = validate_fraction(fraction)

		self.assertEqual(result, False)

	def test_with_given_tuple_with_not_number_element_should_return_false(self):
		fraction = ('str', 25)

		result = validate_fraction(fraction)

		self.assertEqual(result, False)

	def test_with_fraction_with_denominator_zero_should_return_false(self):
		fraction = (25, 0)

		result = validate_fraction(fraction)

		self.assertEqual(result, False)

	def test_with_valid_fraction_should_return_true(self):
		fraction = (25, 2)

		result = validate_fraction(fraction)

		self.assertEqual(result, True)

class TestFindDividersOfNumber(unittest.TestCase):

	def test_with_given_number_should_return_dividers_of_number(self):
		number = 24

		result = find_dividers_of_number(number)
		expected = {2, 3, 4, 6, 8, 12, 24}

		self.assertEqual(result, expected)


class TestSimplifyFraction(unittest.TestCase):
	
	def test_with_given_correct_fraction_should_simplify(self):
		fraction = (4, 8)

		result = simplify_fraction(fraction)

		expected = (1, 2)

		self.assertEqual(result, expected)

	def test_with_irreducable_fraction_should_return_same(self):
		fraction = (1, 7)

		result = simplify_fraction(fraction)

		self.assertEqual(result, fraction)

	def test_wtih_equal_nominator_denominator_of_fraction_should_return_tuple_one_one(self):
		fraction = (9, 9)

		result = simplify_fraction(fraction)

		expected = (1, 1)

		self.assertEqual(result, expected)

	def test_with_invalid_fraction_should_raise_exception(self):
		fraction = (25, 0)

		exc = None

		try:
			result = simplify_fraction(fraction)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid fraction given!')


if __name__ == '__main__':
	unittest.main()