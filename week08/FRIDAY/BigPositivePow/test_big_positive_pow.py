import unittest
from unittest.mock import Mock
from unittest.mock import patch
from big_positive_pow import big_positive_pow


class TestBigPositivePow(unittest.TestCase):
    def test_with_y_less_than_10_should_raise_ValueError(self):

        # with patch('calendar.datetime.datetime') as datetime_mock:
        #     sunday = datetime(year=2020, month=4, day=26)
        #     datetime_mock.today.return_value = sunday
        #     self.assertFalse(is_weekday())

        with patch('big_positive_pow.big_positive_pow') as big_positive_pow_mock:

            big_positive_pow_mock.y.return_value = 0

            result = None
            exc = None
            try:
                result = big_positive_pow_mock()
            except Exception as e:
                exc = e

            print(result)
            # self.assertIsNotNone(exc)
            # self.assertEqual(str(exc), 'Try again.')


if __name__ == '__main__':
    unittest.main()
