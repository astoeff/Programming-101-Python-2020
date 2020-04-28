import unittest
from datetime import datetime, timedelta
from cancellation_policy import validate_conditions
from cancellation_policy import ensure_conditions
from cancellation_policy import sort_conditions
from cancellation_policy import get_current_condition
from cancellation_policy import get_cancellation_fee, get_cancellation_policy
from unittest.mock import Mock


class TestValidateConditions(unittest.TestCase):
    def test_validation_passes_with_valid_conditions(self):
        conditions = [
            {'hours': 10, 'percent': 10},
            {'percent': 100}
        ]

        validate_conditions(conditions)

    def test_raises_exception_if_all_conditions_have_hours(self):
        conditions = [
            {'hours': 10, 'percent': 10}
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

    def test_raises_exception_if_more_than_one_condition_with_no_hours(self):
        conditions = [
            {'hours': 10, 'percent': 100},
            {'percent': 10},
            {'percent': 100}
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

    def test_raises_exception_if_hours_bigger_than_24(self):
        # ARRANGE
        conditions = [
            {'hours': 72, 'percent': 100},
            {'percent': 10},
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:

            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Hours cannot be > 24.')

    def test_raises_exception_if_percent_bigger_than_100(self):
        # ARRANGE
        conditions = [
            {'hours': 23, 'percent': 10000},
            {'percent': 10},
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:

            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Percent cannot be > 100%')

    def test_raises_exception_if_percent_less_than_0(self):
        # ARRANGE
        conditions = [
            {'hours': 23, 'percent': -10},
            {'percent': 10},
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:

            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Percent cannot be < 0%')


class TestEnsureConditions(unittest.TestCase):

    def test_ensure_works_correctly(self):
        conditions = [
            {'hours': 10, 'percent': 10000},
            {'percent': 100}
        ]

        conditions = ensure_conditions(conditions)

        expected = [
            {'hours': 10, 'percent': 10000},
            {'hours': 0, 'percent': 100}
        ]

        self.assertEqual(conditions, expected)


class TestSortConditions(unittest.TestCase):
    def test_if_given_conditions_sorted_in_decreasing_order_by_hours(self):
        conditions = [
            {'hours': 12, 'percent': 50},
            {'hours': 24, 'percent': 10},
            {'hours': 0, 'percent': 100},
            {'hours': 6, 'percent': 80}
        ]

        sorted_conditions = sort_conditions(conditions)

        expected = [
            { 'hours' : 24, 'percent' : 10 },
            { 'hours' : 12, 'percent' : 50 },
            { 'hours' : 6, 'percent': 80 },
            { 'hours' : 0, 'percent' : 100 }
        ]
 
        self.assertEqual(sorted_conditions,expected)


class TestGetCurrentCondition(unittest.TestCase):

    def test_get_current_condition_with_more_than_two_elements_with_value_in_range(self):

        conditions = [
            { 'hours' : 24, 'percent' : 10 },
            { 'hours' : 12, 'percent' : 50 },
            { 'hours' : 6, 'percent': 80 },
            { 'hours' : 0, 'percent' : 100 }
        ]

        now = datetime.now()
        booking_start = now + timedelta(hours=10)

        percent = get_current_condition(conditions, booking_start, now)

        self.assertEqual(percent,80)

    def test_get_current_condition_with_more_than_two_elements_with_value_24(self):

        conditions = [
            { 'hours' : 24, 'percent' : 10 },
            { 'hours' : 12, 'percent' : 50 },
            { 'hours' : 6, 'percent': 80 },
            { 'hours' : 0, 'percent' : 100 }
        ]

        now = datetime.now()
        booking_start = now + timedelta(hours=24)

        percent = get_current_condition(conditions, booking_start, now)

        self.assertEqual(percent,10)

    def test_get_current_condition_with_more_than_two_elements_with_value_equal_to_inner_hours(self):

        conditions = [
            { 'hours' : 24, 'percent' : 10 },
            { 'hours' : 12, 'percent' : 50 },
            { 'hours' : 6, 'percent': 80 },
            { 'hours' : 0, 'percent' : 100 }
        ]

        now = datetime.now()
        booking_start = now + timedelta(hours=12)

        percent = get_current_condition(conditions, booking_start, now)

        self.assertEqual(percent,80)

    def test_get_current_condition_with_more_than_two_elements_with_value_equal_to_first_value_more_than_0(self):

        conditions = [
            { 'hours' : 24, 'percent' : 10 },
            { 'hours' : 12, 'percent' : 50 },
            { 'hours' : 6, 'percent': 80 },
            { 'hours' : 0, 'percent' : 100 }
        ]

        now = datetime.now()
        booking_start = now + timedelta(hours=6)

        percent = get_current_condition(conditions, booking_start, now)

        self.assertEqual(percent,100)

    # def test_get_current_condition_with_more_than_two_elements_with_value_0(self):

    #     conditions = [
    #         { 'hours' : 24, 'percent' : 10 },
    #         { 'hours' : 12, 'percent' : 50 },
    #         { 'hours' : 6, 'percent': 80 },
    #         { 'hours' : 0, 'percent' : 100 }
    #     ]

    #     now = datetime.now()
    #     booking_start = now + timedelta(hours=0)

    #     percent = get_current_condition(conditions, booking_start, now)

    #     self.assertEqual(percent,100)

    def test_get_current_condition_with_one_element_with_given_value_equal_to_the_element(self):
        conditions = [
            {'hours': 0, 'percent': 10}
        ]
        
        now = datetime.now()
        booking_start = now + timedelta(hours=0)

        percent = get_current_condition(conditions, booking_start, now)

        self.assertEqual(percent,10)

    def test_get_current_condition_with_one_element_with_given_value_more_than_the_element(self):
        conditions = [
            {'hours': 0, 'percent': 10}
        ]
        
        now = datetime.now()
        booking_start = now + timedelta(hours=10)

        percent = get_current_condition(conditions, booking_start, now)

        self.assertEqual(percent,10)

    def test_get_current_condition_with_one_element_with_given_value_more_than_24_hours(self):
        conditions = [
            {'hours': 0, 'percent': 10}
        ]
        
        now = datetime.now()
        booking_start = now + timedelta(hours=360)

        percent = get_current_condition(conditions, booking_start, now)

        self.assertEqual(percent,10)

    # def test_get_current_condition_with_one_element_with_0(self):
    #     conditions = [
    #         {'hours': 0, 'percent': 10}
    #     ]
        
    #     now = datetime.now()
    #     booking_start = now + timedelta(hours=0)

    #     percent = get_current_condition(conditions, booking_start, now)

    #     self.assertEqual(percent,10)

    def test_get_current_condition_with_two_elements_with_given_value_more_than_the_upper_boundary(self):
        conditions = [
            {'hours' : 10, 'percent': 20},
            {'hours' : 0, 'percent': 100}
        ]

        now = datetime.now()
        booking_start = now + timedelta(hours=20)

        percent = get_current_condition(conditions, booking_start, now)

        self.assertEqual(percent,20)

    def test_get_current_condition_with_two_elements_with_given_value_equal_to_the_upper_boundary(self):
        conditions = [
            {'hours' : 10, 'percent': 20},
            {'hours' : 0, 'percent': 100}
        ]

        now = datetime.now()
        booking_start = now + timedelta(hours=10)

        percent = get_current_condition(conditions, booking_start, now)

        self.assertEqual(percent,100)

    def test_get_current_condition_with_two_elements_with_given_value_between_the_two_boundaries(self):
        conditions = [
            {'hours' : 10, 'percent': 20},
            {'hours' : 0, 'percent': 100}
        ]

        now = datetime.now()
        booking_start = now + timedelta(hours=5)

        percent = get_current_condition(conditions, booking_start, now)

        self.assertEqual(percent,100)

    # def test_get_current_condition_with_two_elements_with_given_value_0(self):
    #     conditions = [
    #         {'hours' : 10, 'percent': 20},
    #         {'hours' : 0, 'percent': 100}
    #     ]

    #     now = datetime.now()
    #     booking_start = now + timedelta(hours=0)

    #     percent = get_current_condition(conditions, booking_start, now)

    #     self.assertEqual(percent,100)


class TestGetCancellationFee(unittest.TestCase):

    def test_cancellation_fee(self):
        price = 5000
        percent = 10

        result = get_cancellation_fee(price, percent)

        self.assertEqual(500, result)


class TestCancellationPolicy(unittest.TestCase):
    def test_with_given_correct_data_should_calculate_correctly(self):
        # current_time = datetime(2020, 4, 27, 14, 0, 22, 599054)
        c_t = datetime.datetime(year=2020, month=4, day=24)

        datetime = Mock()
        datetime.now.return_value = c_t

        now = datetime.now()
        booking_start = now + timedelta(hours=0)
        price = 1000
        conditions = [
            {'hours': 24, 'percent': 10},
            {'hours': 12, 'percent': 50},
            {'hours': 6, 'percent': 80},
            {'percent': 100}
        ]

        result = get_cancellation_policy(
            conditions,
            price,
            booking_start,
            now
        )

        assertEqual(result, price)



if __name__ == '__main__':
    unittest.main()