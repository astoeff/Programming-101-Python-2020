import unittest
from Fraction import Fraction
from Fraction import __init__
from Fraction import simplify_fraction

class TestFractionInitialisation(unittest.TestCase):
	def test_with_given_non_tuple_fraction_should_raise_exception(self):
		tuple_fraction = None

		exc = None

		try:
			fraction = Fraction(tuple_fraction)
		except Exception as e:
			exc = e
					
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid Fraction given!')

	def test_with_given_tuple_with_not_two_elements_should_raise_exception(self):
		tuple_fraction = (1, 3, 5)

		exc = None

		try:
			fraction = Fraction(tuple_fraction)
		except Exception as e:
			exc = e
					
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid Fraction given!')

	def test_with_given_tuple_with_not_number_element_should_raise_exception(self):
		tuple_fraction = ('str', 25)

		exc = None

		try:
			fraction = Fraction(tuple_fraction)
		except Exception as e:
			exc = e
					
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid Fraction given!')

	def test_with_fraction_with_denominator_zero_should_raise_exception(self):
		tuple_fraction = (25, 0)

		exc = None

		try:
			fraction = Fraction(tuple_fraction)
		except Exception as e:
			exc = e
					
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid Fraction given!')

	def test_with_valid_fraction_should_return_fraction_initialised(self):
		tuple_fraction = (25, 2)

		fraction = Fraction(tuple_fraction)

		self.assertEqual(fraction.tuple_fraction, tuple_fraction)

class TestSimplifyFraction(unittest.TestCase):
	
	def test_with_given_correct_fraction_should_simplify(self):
		fraction = Fraction((4, 8))

		fraction.simplify_fraction()

		expected = Fraction((1, 2))

		self.assertEqual(fraction, expected)

	def test_with_irreducable_fraction_should_return_same(self):
		fraction = Fraction((1, 7))

		fraction.simplify_fraction()

		self.assertEqual(fraction, fraction)

	def test_wtih_equal_nominator_denominator_of_fraction_should_return_fraction_tuple_one_one(self):
		fraction = Fraction((9, 9))

		fraction.simplify_fraction()

		expected = Fraction((1, 1))

		self.assertEqual(fraction, expected)

class TestDunderEq(unittest.TestCase):

	def test_with_given_copy_of_fraction_should_return_equal(self):
		fraction = Fraction((1,2))
		fraction_copy = fraction

		self.assertEqual(fraction, fraction_copy)

	def test_with_given_2_equal_fractions_should_return_equal(self):
		fraction_first = Fraction((1, 2))
		fraction_second = Fraction((1, 2))

		self.assertEqual(fraction_first, fraction_second)

	def test_with_given_2_different_fractions_should_return_not_equal(self):
		fraction_first = Fraction((1, 2))
		fraction_second = Fraction((1, 3))

		self.assertNotEqual(fraction_first, fraction_second)

class TestCollectFractions(unittest.TestCase):

	def test_with_given_2_fractions_should_return_collected_fraction_simplified(self):
		fraction_first = Fraction((1, 7))
		fraction_second = Fraction((2, 6))
		
		result = fraction_first + fraction_second

		expected = Fraction((10, 21))

		self.assertEqual(result, expected)

class TestPrintFraction(unittest.TestCase):

	def test_with_given_fraction_should_print_correctly(self):
		fraction = Fraction((1, 3))

		self.assertEqual(str(fraction), ('1/3'))

class TestSortFractions(unittest.TestCase):

	def test_with_given_list_of_fractions_should_return_sorted_list(self):
		fractions = [Fraction((2,4)), Fraction((1, 3))]

		fractions_sorted = sorted(fractions)

		expected = [Fraction((1, 3)), Fraction((2,4))]

		self.assertEqual(fractions_sorted, expected)

	def test_with_given_list_of_equal_fractions_should_return_same(self):
		fractions = [Fraction((2,4)), Fraction((2, 4)), Fraction((2, 4))]

		fractions_sorted = sorted(fractions)

		self.assertEqual(fractions_sorted, fractions)

	def test_with_given_list_of_more_than_two_fractions_should_return_sorted(self):
		fractions = [Fraction((2,4)), Fraction((2, 5)), Fraction((2, 3)), Fraction((1, 7))]

		fractions_sorted = sorted(fractions)

		expected = [Fraction((1, 7)), Fraction((2,5)), Fraction((2,4)), Fraction((2,3))]


		self.assertEqual(fractions_sorted, expected)

	def test_with_given_list_of_more_than_two_fractions_and_reverse_order_should_return_sorted_in_descending(self):
		fractions = [Fraction((2,4)), Fraction((2, 5)), Fraction((2, 3)), Fraction((1, 7))]

		fractions_sorted = sorted(fractions, reverse = True)

		expected = [Fraction((2, 3)), Fraction((2,4)), Fraction((2,5)), Fraction((1,7))]


		self.assertEqual(fractions_sorted, expected)

if __name__ == '__main__':
	unittest.main()