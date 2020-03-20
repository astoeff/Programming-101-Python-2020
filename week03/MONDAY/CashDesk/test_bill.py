import unittest
from bill import Bill

class TestBillConstructor(unittest.TestCase):
	def test_with_given_non_integer_amount_should_raise_exception(self):
		amount = None
		
		exc = None
		try:
			bill = Bill(amount)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid argument given, amount should be int!')

	def test_with_given_negative_integer_amount_should_raise_exception(self):
		amount = -10
		
		exc = None
		try:
			bill = Bill(amount)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid argument given, amount should be positive int!')

	def test_with_given_zero_amount_should_raise_exception(self):
		amount = 0
		
		exc = None
		try:
			bill = Bill(amount)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid argument given, amount should be positive int!')


	def test_with_given_integer_amount_should_create_instance(self):
		amount = 10		
		
		bill = Bill(amount)
	
		self.assertEqual(bill.amount, amount)
		self.assertEqual(type(bill), Bill)

class TestStringRepresentationOfBill(unittest.TestCase):
	def test_with_given_bill_should_represent_in_string_correctly(self):
		bill = Bill(10)

		self.assertEqual(str(bill), "A 10$ bill")

class TestStringRepresentationOfBill(unittest.TestCase):
	def test_with_given_bill_should_represent_in_string_correctly(self):
		bill = Bill(10)

		self.assertEqual(str(bill), "A 10$ bill")
class TestRepresentationOfBill(unittest.TestCase):
	def test_with_given_bill_should_represent_correctly(self):
		bill = Bill(10)

		self.assertEqual(bill, Bill(10))

class TestIntRepresentationOfBill(unittest.TestCase):
	def test_with_given_bill_should_represent_in_int_correctly(self):
		amount = 20
		bill = Bill(amount)
		
		bill_to_int = int(bill)

		self.assertEqual(bill_to_int, amount)

class TestEqualDunderOfBill(unittest.TestCase):
	def test_with_given_same_reference_of_bill_should_return_that_are_equal(self):
		bill = Bill(10)
		bill_ref = bill

		self.assertEqual(bill, bill_ref)

	def test_with_given_two_bills_with_same_amounts_should_return_that_are_equal(self):
		amount = 10
		bill_lhs = Bill(amount)
		bill_rhs = Bill(amount)

		self.assertEqual(bill_lhs, bill_rhs)

	def test_with_given_two_bills_with_different_amounts_should_return_that_are_not_equal(self):
		amount_lhs = 10
		amount_rhs = 20
		bill_lhs = Bill(amount_lhs)
		bill_rhs = Bill(amount_rhs)

		self.assertNotEqual(bill_lhs, bill_rhs)

class TestHashDunderOfBill(unittest.TestCase):
	def test_with_given_map_of_bills_should_work_correctly(self):
		money_holder = {}
		bill = Bill(10)

		money_holder[bill] = 1 

		money_holder[bill] += 1

		self.assertEqual(money_holder[bill], 2)



if __name__ == '__main__':
	unittest.main()