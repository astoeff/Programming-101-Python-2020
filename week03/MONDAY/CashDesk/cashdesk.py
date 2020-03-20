from bill import Bill
from bill_batch import BillBatch

class Cashdesk:
	def __init__(self):
		self.money_table = {}

	def __take_bill(self, bill):
		if bill in self.money_table:
				self.money_table[bill] += 1
		else:
				self.money_table[bill] = 1

	def take_money(self, money):
		if type(money) != Bill and type(money) != BillBatch:
			raise TypeError('Invalid argument given, argument needs to be instance of Bill or BillBatch')
		if type(money) == Bill:
			self.__take_bill(money)
		else:
			for bill in money.batch:
				self.__take_bill(bill)

	def total(self):
		return sum(bill.amount * self.money_table[bill] for bill in self.money_table.keys())

	def __repr__(self):
		representation = ''
		list_of_money_in_table = [i for i in self.money_table]
		sorted_list = sorted(list_of_money_in_table, key = lambda c:c.amount)
		for el in sorted_list:
			representation += str(str(el)[2:]) + 's - ' + str(self.money_table[el]) + '\n'
		return representation	

	def inspect(self):
		print(self.__repr__())	
		# return self.__repr__()   #used for unit testing


if __name__ == '__main__':
	cashdesk = Cashdesk()

	cashdesk.take_money(Bill(10))
	batch = BillBatch([Bill(i) for i in range(1,5)])
	cashdesk.take_money(batch)
	cashdesk.inspect()

	values = [10, 20, 50, 100, 100, 100]
	bills = [Bill(value) for value in values]

	batch = BillBatch(bills)

	desk = Cashdesk()

	desk.take_money(batch)
	desk.take_money(Bill(10))

	print(desk.total()) # 390
	desk.inspect()