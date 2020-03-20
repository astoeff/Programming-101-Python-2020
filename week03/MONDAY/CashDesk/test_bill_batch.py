import unittest
from bill import Bill
from bill_batch import BillBatch

class TestBillBatchInitialisation(unittest.TestCase):
	def test_with_given_non_list_as_argument_should_raise_exception(self):
		bill_batch_argment = None

		exc = None
		try:
			batch = BillBatch(bill_batch_argment)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid argument given, argument needs to be of type list!')

	def test_with_given_list_of_non_bills_as_argument_should_raise_exception(self):
		bill_batch_argment = [1, 2, 3]

		exc = None
		try:
			batch = BillBatch(bill_batch_argment)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid element of list given, argument needs to be list of elements of type Bill!')

	def test_with_given_list_of_bills_as_argument_should_raise_exception(self):
		bill_one = Bill(10)
		bill_two = Bill(20)
		bill_batch_argment = [bill_one, bill_two]

		batch = BillBatch(bill_batch_argment)
		
		self.assertEqual(type(batch), BillBatch)
		self.assertEqual(batch.batch, bill_batch_argment)

# __len__(self) - returns the number of Bills in the batch

class TestLenDunderOfBillBatch(unittest.TestCase):
	def test_with_given_bill_batch_with_zero_elements_should_return_zero_as_length_of_batch(self):
		batch = BillBatch([])

		length = len(batch)

		self.assertEqual(length,len(batch.batch))

	def test_with_given_bill_batch_with_more_than_zero_elements_should_return_length_of_batch(self):
		batch = BillBatch([Bill(i) for i in range(1,5)])

		length = len(batch)

		self.assertEqual(length,len(batch.batch))

class TestIteratingOverBillBatch(unittest.TestCase):
	def test_with_given_bill_batch_should_be_available_for_iteration(self):
		batch = BillBatch([Bill(i) for i in range(1,5)])

		result = []
		for bill in batch:
			result.append(bill.amount)

		expected = [1, 2, 3, 4]

		self.assertEqual(result, expected)

	def test_with_given_bill_batch_should_be_available_to_return_bill_by_given_index(self):
		batch = BillBatch([Bill(i) for i in range(1,5)])

		result = batch[2]		

		expected = Bill(3) #bill on pos 2 is A 3$ bill

		self.assertEqual(result, expected)

class TestTotalMethodOfBillBatch(unittest.TestCase):
	def test_with_given_bill_batch_should_return_total_sum_of_bills(self):
		batch = BillBatch([Bill(i) for i in range(1,5)]) #bills with values: 1, 2, 3, 4 

		result = batch.total()

		expected = 10

		self.assertEqual(result, expected)


if __name__ == '__main__':
	unittest.main() 