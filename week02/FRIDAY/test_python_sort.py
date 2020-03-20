import unittest
from python_sort import my_sort
from python_sort import is_iterable
from python_sort import check_is_list_of_dictionaries_given
from python_sort import check_if_iterable_is_homogene
from python_sort import check_if_key_is_in_all_dictionaries_in_iterable
from python_sort import sort_dictionary

class TestMySort(unittest.TestCase):

	def test_with_no_arguments_should_return_empty_list(self):
		result = my_sort()
		expected = []
		self.assertEqual(result, expected)

	def test_with_given_not_homogene_iterable_should_raise_exception(self):
		given = (1, 2, 'str')

		err = None
		try:
			result = my_sort(given,False)
		except Exception as e:
			err = e
	
		self.assertEqual(str(err), 'Iterable is not homogene!')

	def test_with_no_iterable_and_ascending_false_should_return_empty_list(self):
		result = my_sort(ascending = False)
		expected = []
		self.assertEqual(result, expected)

	def test_with_no_iterable_and_given_key_should_return_empty_list(self):
		result = my_sort(key = 'age')
		expected = []
		self.assertEqual(result, expected)

	def test_with_given_invalid_iterable_should_raise_exception(self):
		given_ivalid = {1 : 'one'}

		exc = None

		# ACT
		try:
			result = my_sort(given_ivalid)
		except Exception as err:
			exc = err

		# ASSERTS
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid iterable given!')


	def test_with_given_list_should_sort_in_ascending(self):
		given_list = [5, 8, 2, 0, 16]

		result = my_sort(given_list)
		expected = [0, 2, 5, 8, 16]

		self.assertEqual(result,expected)

	def test_with_given_tuple_should_sort_in_ascending(self):
		given_tuple = (5, 8, 2, 0, 16)

		result = my_sort(given_tuple)
		expected = (0, 2, 5, 8, 16)

		self.assertEqual(result,expected)

	def test_with_given_ordered_list_in_ascending_only_should_return_same(self):
		ordered = [1, 2, 3, 4]

		result = my_sort(ordered)

		self.assertEqual(ordered, result)

	def test_with_given_ordered_tuple_in_ascending_only_should_return_same(self):
		ordered = (1, 2, 3, 4)

		result = my_sort(ordered)

		self.assertEqual(ordered, result)

	def test_with_given_list_and_descending_order_shpuld_send_in_descending_order(self):
		given_list = [4, 2, 6, 20]

		result = my_sort(given_list, False)
		expected = [20, 6, 4, 2]

		self.assertEqual(result, expected)	
		
	def test_with_given_tuple_and_descending_order_should_sort_in_descending_order(self):
		given_tuple = (4, 2, 6, 20)

		result = my_sort(given_tuple, False)
		expected = (20, 6, 4, 2)

		self.assertEqual(result, expected)

	def test_with_given_list_of_dictionaries_existing_key_and_default_order_should_sort_in_ascending_order(self):
		dictionary = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
		key = 'age'

		result = my_sort(dictionary, key = key)
		expected = [{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}]

		self.assertEqual(result,expected)

	def test_with_given_tuple_of_dictionaries_existing_key_and_default_order_should_sort_in_ascending_order(self):
		dictionary = ({'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25})
		key = 'age'

		result = my_sort(dictionary, key = key)
		expected = ({'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27})

		self.assertEqual(result,expected)

	def test_with_given_list_of_dictionaries_existing_key_and_ascending_order_should_sort_in_ascending_order(self):
		dictionary = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
		key = 'age'
		ascending = True

		result = my_sort(dictionary, ascending, key)
		expected = [{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}]

		self.assertEqual(result,expected)

	def test_with_given_tuple_of_dictionaries_existing_key_and_ascending_order_should_sort_in_ascending_order(self):
		dictionary = ({'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25})
		key = 'age'
		ascending = True

		result = my_sort(dictionary, ascending, key)
		expected = ({'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27})

		self.assertEqual(result,expected)

	def test_with_given_list_of_dictionaries_existing_key_and_descending_order_should_sort_in_descending_order(self):
		dictionary = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
		key = 'age'
		ascending = False

		result = my_sort(dictionary, ascending, key)
		expected = [{'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}, {'name': 'Marto', 'age': 24}]

		self.assertEqual(result,expected)

	def test_with_given_tuple_of_dictionaries_existing_key_and_descending_order_should_sort_in_descending_order(self):
		dictionary = ({'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25})
		key = 'age'
		ascending = False

		result = my_sort(dictionary, ascending, key)
		expected = ({'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}, {'name': 'Marto', 'age': 24})

		self.assertEqual(result,expected)

	def test_with_given_list_of_dictionaries_with_default_key_should_return_same(self):
		given = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]

		result = my_sort(given)

		self.assertEqual(given,result)

	def test_with_given_tuple_of_dictionaries_with_default_key_should_return_same(self):
		given = ({'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25})

		result = my_sort(given)

		self.assertEqual(given,result)

	def test_with_given_list_of_dictionaries_with_key_not_in_all_should_raise_exception(self):
		given = [{'name': 'Marto', 'age': 24}, {}, {'name': 'Sashko', 'age': 25}]
		key= 'age'
		
		exc = None

		# ACT
		try:
			result = my_sort(given, key = key)
		except Exception as err:
			exc = err

		# ASSERTS

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Key age not in all dictionaries!')

	def test_with_given_tuple_of_dictionaries_with_key_not_in_all_should_raise_exception(self):
		given = ({'name': 'Marto', 'age': 24}, {}, {'name': 'Sashko', 'age': 25})
		key = 'age'
		
		exc = None

		# ACT
		try:
			result = my_sort(given, key = key)
		except Exception as err:
			exc = err

		# ASSERTS

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Key {k} not in all dictionaries!'.format(k = key))

	def test_with_given_list_of_dictionaries_with_key_not_string_should_raise_exception(self):
		given = [{'name': 'Marto', 27 : 24}, {27 : 25}, {'name': 'Sashko', 27 : 25}]
		key= 27
		
		exc = None

		# ACT
		try:
			result = my_sort(given, key = key)
		except Exception as err:
			exc = err

		# ASSERTS

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Key {k}: not a string!'.format(k = key))

	def test_with_given_tuple_of_dictionaries_with_key_not_string_should_raise_exception(self):
		given = ({'name': 'Marto', 27 : 24}, {27 : 25}, {'name': 'Sashko', 27 : 25})
		key= 27
		
		exc = None

		# ACT
		try:
			result = my_sort(given, key = key)
		except Exception as err:
			exc = err

		# ASSERTS

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Key {k}: not a string!'.format(k = key))


class TestIsIterableListOrTuple(unittest.TestCase):

	def test_with_given_list_should_return_string_list(self):
		given_list = [1,2,4]

		result = is_iterable(given_list)

		self.assertEqual(result,'list')

	def test_with_given_tuple_should_return_string_tuple(self):
		given_tuple = ()

		result = is_iterable(given_tuple)

		self.assertEqual(result, 'tuple')

	def test_with_given_other_type_should_return_string_invalid_type(self):
		given = 'invalid type'

		result = is_iterable(given)

		self.assertEqual(result, 'invalid type')

class TestCheckIsListOfDictionariesGiven(unittest.TestCase):
	
	def test_with_given_list_of_dicitonaries(self):
		given = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]		

		result = check_is_list_of_dictionaries_given(given)

		self.assertEqual(result,True)

	def test_with_given_list_of_not_only_dicitonaries(self):
		given = [{'name': 'Marto', 'age': 24}, 5, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]		

		result = check_is_list_of_dictionaries_given(given)

		self.assertEqual(result,False)

class TestCheckIfIterableIsHomogene(unittest.TestCase):

	def test_with_given_homogene_iterable(self):
		given = [1, 2, 3]

		result = check_if_iterable_is_homogene(given)

		self.assertEqual(result, True)

	def test_with_given_not_homogene_iterable(self):
		given = [1, 2, 'str']

		result = check_if_iterable_is_homogene(given)

		self.assertEqual(result, False)

class TestCheckIfKeyIsInAllDictionariesInIterable(unittest.TestCase):

	def test_with_given_key_in_all_dictionaries(self):		
		given = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
		key = 'age'
		
		result = check_if_key_is_in_all_dictionaries_in_iterable(given,key)

		self.assertEqual(result,True)

	def test_with_given_key_not_in_all_dictionaries(self):		
		given = [{'name': 'Marto', 'age': 24}, {}, {'name': 'Sashko', 'age': 25}]
		key = 'age'
		
		result = check_if_key_is_in_all_dictionaries_in_iterable(given,key)

		self.assertEqual(result,False)

class TestSortDictionary(unittest.TestCase):

	def test_with_given_ascending_order(self):
		given = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
		key = 'age'
		ascending = True
		
		result = sort_dictionary(given, ascending, key)
		expected = [{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}]

		self.assertEqual(result, expected)

	def test_with_given_descending_order(self):
		given = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
		key = 'age'
		ascending = False
		
		result = sort_dictionary(given, ascending, key)
		expected = [{'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}, {'name': 'Marto', 'age': 24}]

		self.assertEqual(result, expected)


if __name__ == '__main__':
	unittest.main()