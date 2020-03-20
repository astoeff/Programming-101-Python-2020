import unittest
from collect_fractions import collect_fractions
from collect_fractions import validate_fractions
from collect_fractions import find_lcm_of_numbers
from collect_fractions import modify_nominators


class TestValidateFractions(unittest.TestCase):

	 def test_with_given_not_list_of_tuples_should_return_false(self):
	 	given = ((1, 2), (1, 5))

	 	result = validate_fractions(given)

	 	self.assertEqual(result, False)

	 def test_with_given_empty_list_should_return_false(self):
	 	given = []

	 	result = validate_fractions(given)

	 	self.assertEqual(result, False)

	 def test_with_given_invalid_fractions_should_return_false(self):
	 	given = [('str', 1)]

	 	result = validate_fractions(given)

	 	self.assertEqual(result, False)

	 def test_with_given_valid_fractions_should_return_true(self):
	 	given = [(5, 1)]

	 	result = validate_fractions(given)

	 	self.assertEqual(result, True)

class TestFindLCMOfNumbers(unittest.TestCase):

	def test_with_given_only_one_number_should_return_given_number(self):
		given = [1]

		result = find_lcm_of_numbers(given)

		self.assertEqual(result, 1)

	def test_with_given_two_numbers_should_return_lcm_of_numbers(self):
		given = [7, 6]

		result = find_lcm_of_numbers(given)

		self.assertEqual(result, 42)

class TestModifyNominators(unittest.TestCase):

	def test_with_given_two_nominators_should_return_modified_nominators(self):
		nominators = [2, 7]
		denominators = [7, 6]
		lcm = 42

		result = modify_nominators(nominators, denominators, lcm)
		expected = [12, 49]

		self.assertEqual(result, expected)

	def test_with_given_more_than_two_nominators_should_return_modified_nominators(self):
		nominators = [2, 7, 5, 4]
		denominators = [7, 6, 2, 5]
		lcm = 210

		result = modify_nominators(nominators, denominators, lcm)
		expected = [60, 245, 525, 168]

		self.assertEqual(result, expected)


class TestCollectFractions(unittest.TestCase):
	def test_with_given_non_list_of_fractions_should_raise_exception(self):
		fractions = None

		exc = None
		try:
			result = collect_fractions(fractions)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid fractions given!')

	def test_with_given_empty_list_of_fractions_should_raise_exception(self):
		fractions = []

		exc = None
		try:
			result = collect_fractions(fractions)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid fractions given!')

	def test_with_given_list_of_fractions_with_non_integer_element_of_fraction_should_raise_exception(self):
		fractions = [('str', 2), (5, 25)]

		exc = None
		try:
			result = collect_fractions(fractions)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid fractions given!')

	def test_with_given_list_of_fractions_with_zero_denominator_of_fraciton_should_raise_exception(self):
		fractions = [(24, 2), (5, 0)]

		exc = None
		try:
			result = collect_fractions(fractions)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid fractions given!')

	def test_with_given_list_of_one_fraciton_should_return_given_fraction_simplified(self):
		fractions = [(4, 8)]

		
		result = collect_fractions(fractions)
		expected = [(4, 8)]

		self.assertEqual(result, expected)

	def test_with_given_list_of_two_fracitons_should_return_collected_fraction_simplified(self):
		fractions = [(1, 7), (2, 6)]

		
		result = collect_fractions(fractions)
		expected = (10, 21)

		self.assertEqual(result, expected)

	def test_with_given_list_of_more_than_two_fracitons_should_return_collected_fraction_simplified(self):
		fractions = [(2, 5), (3, 6), (5, 3)]

		
		result = collect_fractions(fractions)
		expected = (77, 30)

		self.assertEqual(result, expected)


if __name__ == '__main__':
	unittest.main()