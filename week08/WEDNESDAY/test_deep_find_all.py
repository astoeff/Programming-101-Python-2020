import unittest
from deep_find_all import deep_find_all


class TestDeepFindAll(unittest.TestCase):
    def test_with_given_non_nested_dict_with_searched_value_occurce_once_in_it_should_find_correctly(self):
        data = {'data1': 20, 'data2': 200.4, 'result': 42}
        key = 'result'

        result = [42]

        self.assertEqual(result, deep_find_all(data, key))

    def test_with_given_non_nested_dict_with_searched_value_occurce_more_than_once_in_it_should_find_correctly(self):
        data = {'data1': 20, 'data2': 200.4, 'data3': {'result': 42, 'data4': 52}, 'result': 52}
        key = 'result'

        result = [42, 52]

        self.assertEqual(result, deep_find_all(data, key))


if __name__ == '__main__':
    unittest.main()
