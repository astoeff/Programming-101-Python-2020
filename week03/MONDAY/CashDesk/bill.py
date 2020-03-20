class Bill:
	def __init__(self, amount):
		if type(amount) != int:
			raise TypeError('Invalid argument given, amount should be int!')
		if amount <= 0:
				raise ValueError('Invalid argument given, amount should be positive int!')
		self.amount = amount

	def __str__(self):
		return 'A {amount}$ bill'.format(amount = self.amount)

	def __repr__(self):
		return 'A {amount}$ bill'.format(amount = self.amount)

	def __int__(self):
		return self.amount

	def __eq__(self, other):
		return self.amount == other.amount 

	def __hash__(self):
		return hash(self.amount)

	def __add__(self, other):
		return self.amount + other.amount

	def __radd__(self, other):
		return other + self.amount

if __name__ == '__main__':	
	a = Bill(10)
	b = Bill(5)
	c = Bill(10)

	print(int(a)) # 10
	print(str(a)) # "A 10$ bill"
	print(a) # A 10$ bill

	print(a == b) # False
	print(a == c) # True

	money_holder = {}

	money_holder[a] = 1 # We have one 10% bill

	if c in money_holder:
	    money_holder[c] += 1

	print(money_holder) # { "A 10$ bill": 2 }