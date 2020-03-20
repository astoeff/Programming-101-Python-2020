import unittest
from cashdesk import Cashdesk
from bill import Bill
from bill_batch import BillBatch

class TestCashDeskInitialisation(unittest.TestCase):
	def test_with_given_no_arguments_should_instantiate_cashdesk_object(self):
		cashdesk = Cashdesk()

		self.assertEqual(type(cashdesk), Cashdesk)
		self.assertEqual(cashdesk.money_table, {})

# class TestTakeBill(unittest.TestCase):
# 	def test_with_given_empty_cashdesk_and_bill_object_as_argument_should_add_to_table(self):
# 		cashdesk = Cashdesk()
# 		bill = Bill(10)
# 		take_bill_argument = bill
		
# 		cashdesk._take_bill(take_bill_argument)
		
# 		self.assertEqual(cashdesk.money_table[bill], 1)

# 	def test_with_given_non_empty_cashdesk_and_bill_object_as_argument_should_add_to_table(self):
# 		cashdesk = Cashdesk()
# 		bill_10_dollars = Bill(10)
# 		take_bill_argument = bill_10_dollars
# 		cashdesk._take_bill(take_bill_argument)
# 		bill_20_dollars = Bill(20)
# 		take_bill_argument = bill_20_dollars

# 		cashdesk._take_bill(take_bill_argument)
		
# 		self.assertEqual(cashdesk.money_table[bill_20_dollars], 1)

# 	def test_with_given_non_empty_cashdesk_and_bill_object_as_argument_that_exists_in_table_should_icrement_value_in_table(self):
# 		cashdesk = Cashdesk()
# 		bill_10_dollars = Bill(10)
# 		take_bill_argument = bill_10_dollars
# 		cashdesk._take_bill(take_bill_argument)
		
# 		cashdesk._take_bill(take_bill_argument)
		
# 		self.assertEqual(cashdesk.money_table[bill_10_dollars], 2)

class TestTakeMoney(unittest.TestCase):
	def test_with_given_non_bill_or_batch_bill_object_as_argument_should_raise_exception(self):
		cashdesk = Cashdesk()
		take_money_invalid_argument = 'string'

		exc = None
		try:
			cashdesk.take_money(take_money_invalid_argument)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid argument given, argument needs to be instance of Bill or BillBatch')

	def test_with_given_empty_cashdesk_and_bill_object_as_argument_should_add_to_table(self):
		cashdesk = Cashdesk()
		bill = Bill(10)
		take_money_bill_argument = bill
		
		cashdesk.take_money(take_money_bill_argument)
		
		self.assertEqual(cashdesk.money_table[bill], 1)

	def test_with_given_non_empty_cashdesk_and_bill_object_as_argument_should_add_to_table(self):
		cashdesk = Cashdesk()
		bill_10_dollars = Bill(10)
		take_money_bill_argument = bill_10_dollars
		cashdesk.take_money(take_money_bill_argument)
		bill_20_dollars = Bill(20)
		take_money_bill_argument = bill_20_dollars

		cashdesk.take_money(take_money_bill_argument)
		
		self.assertEqual(cashdesk.money_table[bill_20_dollars], 1)
		self.assertEqual(cashdesk.money_table[bill_10_dollars], 1)


	def test_with_given_non_empty_cashdesk_and_bill_object_as_argument_that_exists_in_table_should_icrement_value_in_table(self):
		cashdesk = Cashdesk()
		bill_10_dollars = Bill(10)
		take_money_bill_argument = bill_10_dollars
		cashdesk.take_money(take_money_bill_argument)
		
		cashdesk.take_money(take_money_bill_argument)
		
		self.assertEqual(cashdesk.money_table[bill_10_dollars], 2)

	def test_with_given_empty_cashdesk_and_bill_batch_object_as_argument_should_add_all_bills_in_batch_to_table(self):
		cashdesk = Cashdesk()
		bill_batch = BillBatch([Bill(i) for i in (1,5)])
		take_money_bill_batch_argument = bill_batch
		
		cashdesk.take_money(take_money_bill_batch_argument)
		
		for i in (1,5):
			self.assertEqual(cashdesk.money_table[Bill(i)], 1)

	def test_with_given_non_empty_cashdesk_and_bill_batch_object_as_argument_should_add_to_table(self):
		cashdesk = Cashdesk()
		bill_10_dollars = Bill(10)
		take_money_bill_argument = bill_10_dollars
		cashdesk.take_money(take_money_bill_argument)
		bill_batch = BillBatch([Bill(i) for i in (1,5)])
		take_money_bill_batch_argument = bill_batch
		
		cashdesk.take_money(take_money_bill_batch_argument)
		
		for i in (1,5):
			self.assertEqual(cashdesk.money_table[Bill(i)], 1)
		self.assertEqual(cashdesk.money_table[bill_10_dollars], 1)

	def test_with_given_non_empty_cashdesk_and_bill_batch_object_as_argument_that_all_elements_in_it_exist_in_table_should_icrement_values_in_table(self):
		cashdesk = Cashdesk()
		bill_batch = BillBatch([Bill(i) for i in (1,5)])
		take_money_bill_batch_argument = bill_batch
		cashdesk.take_money(take_money_bill_batch_argument)

		cashdesk.take_money(take_money_bill_batch_argument)

		for i in (1,5):
			self.assertEqual(cashdesk.money_table[Bill(i)], 2)

class TestTotal(unittest.TestCase):
	def test_with_given_empty_cashdesk_should_return_zero(self):
		cashdesk = Cashdesk()

		result = cashdesk.total()

		self.assertEqual(result, 0)

	def test_with_given_one_bill_cashdesk_should_return_amount_of_bill(self):
		cashdesk = Cashdesk()
		amount = 10
		cashdesk.take_money(Bill(amount))

		result = cashdesk.total()

		self.assertEqual(result, amount)

	def test_with_given_multi_bill_cashdesk_should_return_amount_of_all_bills(self):
		cashdesk = Cashdesk()
		cashdesk.take_money(BillBatch([Bill(i) for i in range(1,5)]))
		
		result = cashdesk.total()
		
		expected = sum(range(1,5))

		self.assertEqual(result, expected)

	def test_with_given_multi_bill_cashdesk_and_bill_occurs_more_than_ones_should_return_amount_of_all_bills(self):
		cashdesk = Cashdesk()
		cashdesk.take_money(Bill(10))
		batch = BillBatch([Bill(i) for i in range(1,5)])
		cashdesk.take_money(batch)
		cashdesk.take_money(batch)
		
		result = cashdesk.total()
		
		expected = sum(range(1,5)) * 2 + 10

		self.assertEqual(result, expected)

class TestRepresentation(unittest.TestCase):
	def test_with_given_empty_cashdesk_should_print_empty_string(self):
		cashdesk = Cashdesk()

		expected = ''

		self.assertEqual(cashdesk.__repr__(), expected)

	def test_with_given_one_bill_cashdesk_should_print_correctly(self):
		cashdesk = Cashdesk()
		cashdesk.take_money(Bill(10))

		expected = '10$ bills - 1\n'
		self.assertEqual(cashdesk.__repr__(), expected)

	def test_with_given_multi_bill_cashdesk_should_print_in_ascending_order_of_amount_of_bill(self):
		cashdesk = Cashdesk()

		cashdesk.take_money(Bill(10))
		batch = BillBatch([Bill(i) for i in range(1,5)])
		cashdesk.take_money(batch)

		expected = '1$ bills - 1\n2$ bills - 1\n3$ bills - 1\n4$ bills - 1\n10$ bills - 1\n'

		self.assertEqual(cashdesk.__repr__(), expected)

	def test_with_given_multi_bill_cashdesk_and_bill_occurs_more_than_ones_should_print_in_ascending_order_of_amount_of_bill(self):
		cashdesk = Cashdesk()
		cashdesk.take_money(Bill(10))
		batch = BillBatch([Bill(i) for i in range(1,5)])
		cashdesk.take_money(batch)
		cashdesk.take_money(batch)
		
		expected = '1$ bills - 2\n2$ bills - 2\n3$ bills - 2\n4$ bills - 2\n10$ bills - 1\n'

		self.assertEqual(cashdesk.__repr__(), expected)

# class TestInspect(unittest.TestCase):
# 	def test_with_given_cashdesk_should_print_representation(self):
# 		cashdesk = Cashdesk()
# 		cashdesk.take_money(Bill(10))
# 		batch = BillBatch([Bill(i) for i in range(1,5)])
# 		cashdesk.take_money(batch)
# 		cashdesk.take_money(batch)
		
# 		expected = '1$ bills - 2\n2$ bills - 2\n3$ bills - 2\n4$ bills - 2\n10$ bills - 1\n'

# 		printed = cashdesk.inspect()
# 		self.assertEqual(printed, expected)
		
if __name__ == '__main__':
	unittest.main()

