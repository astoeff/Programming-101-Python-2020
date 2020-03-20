import unittest
from sort_array_of_fractions import sort_fractions

class TestSortFractions(unittest.TestCase):
	def test_with_given_non_list_of_fractions_should_raise_exception(self):
		fractions = None

		exc = None
		try:
			result = sort_fractions(fractions)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid fractions given!')

	def test_with_given_empty_list_of_fractions_should_raise_exception(self):
		fractions = []

		exc = None
		try:
			result = sort_fractions(fractions)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid fractions given!')

	def test_with_given_list_of_fractions_with_non_integer_element_of_fraction_should_raise_exception(self):
		fractions = [('str', 2), (5, 25)]

		exc = None
		try:
			result = sort_fractions(fractions)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid fractions given!')

	def test_with_given_list_of_fractions_with_zero_denominator_of_fraciton_should_raise_exception(self):
		fractions = [(24, 2), (5, 0)]

		exc = None
		try:
			result = sort_fractions(fractions)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid fractions given!')

	def test_with_given_list_of_fractions_with_non_bool_order_should_raise_exception(self):
		fractions = [(24, 2), (5, 2)]

		exc = None
		try:
			result = sort_fractions(fractions, 5)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid order given, needs to be bool!')

	def test_with_given_list_of_one_fraciton_and_ascending_default_should_return_given_fraction(self):
		fractions = [(4, 8)]

		
		result = sort_fractions(fractions)
		expected = [(4, 8)]

		self.assertEqual(result, expected)

	def test_with_given_list_of_one_fraciton_and_ascending_false_should_return_given_fraction(self):
		fractions = [(4, 8)]

		
		result = sort_fractions(fractions, False)
		expected = [(4, 8)]

		self.assertEqual(result, expected)

	def test_with_given_list_of_two_fracitons_and_ascending_default_should_return_sorted__fractions_in_ascending_order(self):
		fractions = [(1, 7), (2, 6)]

		
		result = sort_fractions(fractions)
		expected = [(1, 7), (2, 6)]

		self.assertEqual(result, expected)

	def test_with_given_list_of_two_fracitons_and_ascending_false_should_return_sorted_fractions_in_descending_order(self):
		fractions = [(1, 7), (2, 6)]

		
		result = sort_fractions(fractions, False)
		expected = [(2, 6), (1, 7)]

		self.assertEqual(result, expected)

	def test_with_given_list_of_more_than_two_fracitons_and_ascending_default_should_return_sorted_fractions_in_ascending_order(self):
		fractions = [(5, 3), (2, 5), (3, 6)]

		
		result = sort_fractions(fractions)
		expected = [(2, 5), (3, 6), (5, 3)]

		self.assertEqual(result, expected)

	def test_with_given_list_of_more_than_two_fracitons_and_ascending_true_should_return_sorted_fractions_in_ascending_order(self):
		fractions = [(5, 3), (2, 5), (3, 6)]

		
		result = sort_fractions(fractions, True)
		expected = [(2, 5), (3, 6), (5, 3)]

		self.assertEqual(result, expected)

	def test_with_given_list_of_more_than_two_fracitons_and_ascending_false_should_return_sorted_fractions_in_ascending_order(self):
		fractions = [(5, 3), (2, 5), (3, 6)]

		
		result = sort_fractions(fractions, False)
		expected = [(5, 3), (3, 6), (2, 5)]

		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()