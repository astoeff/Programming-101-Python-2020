import unittest
from deep_find import deep_find


class TestDeepFind(unittest.TestCase):
    def test_with_given_non_nested_dict_should_find_correctly(self):
        data = {'data1': 20, 'data2': 200.4, 'result': 42}
        key = 'result'

        result = 42

        self.assertEqual(result, deep_find(data, key))

    def test_with_given_nested_dict_should_find_correctly(self):
        data = {'data1': 20, 'data2': 200.4, 'data3': {'data4': 2, 'result': 42}}
        key = 'result'

        result = 42

        self.assertEqual(result, deep_find(data, key))

    def test_with_given_multi_nested_dict_should_find_correctly(self):
        data = {'level1_data1': 20, 'level1_data2': 200.4,
                'level1_data3': {'level2_data1': {'level3_data1': {'result': 42, 'non-result': 32}}}}
        key = 'result'

        result = 42

        self.assertEqual(result, deep_find(data, key))

    def test_with_given_list_of_dicts_as_value_in_dict_should_find_correctly(self):
        data = {'data1': 20, 'data2': 200.4, 3: [{'data3': 2, 'result': 42}, {'data4': 7}]}
        key = 'result'

        result = 42

        self.assertEqual(result, deep_find(data, key))

    def test_with_given_nested_list_of_dicts_as_value_in_dict_should_find_correctly(self):
        data = {'data1': 20, 'data2': 200.4,
                3: [{'data3': 2, 'data4': [{'data5': 2, 'result': 42}, {'data6': 8}], 'data7': 7}]}
        key = 'result'

        result = 42

        self.assertEqual(result, deep_find(data, key))

    def test_with_given_tuple_of_dicts_as_value_in_dict_should_find_correctly(self):
        data = {'data1': 20, 'data2': 200.4, 3: ({'data3': 2, 'data4': 7}, {'result': 42, 'data5': 81})}
        key = 'result'

        result = 42

        self.assertEqual(result, deep_find(data, key))

    def test_with_given_nested_tuple_of_dicts_as_value_in_dict_should_find_correctly(self):
        data = {'data1': 20, 'data2': 200.4,
                3: ({'data3': 2, 'data4': ({'data5': 2, 'result': 42}, {'data6': 8}), 'data7': 7})}
        key = 'result'

        result = 42

        self.assertEqual(result, deep_find(data, key))

    # def test_with_given_multi_nesting_with_list_tuples_and_dicts_as_value_should_find_correctly(self):
    #     data = {'level1_data1': [20, {'level2_data1': 200, 'level2_data2': 500}, [{'level2_data3': 12, 'level2_data4': 100}, ({'level3_data1': 2, 'result': 42})]], 'level1_data2': 22}
    #     key = 'result'

    #     result = 42

    #     self.assertEqual(result, deep_find(data, key))

if __name__ == '__main__':
    unittest.main()
