from simplify_fraction import *
from collect_fractions import *

class Fraction:
	def __init__(self, tuple_fraction):
		if validate_fraction(tuple_fraction):
			self.tuple_fraction = tuple_fraction
		else:
			raise ValueError('Invalid Fraction given!')

	def simplify_fraction(self):
		self.tuple_fraction = simplify_fraction(self.tuple_fraction)

	def __add__(self, other):
		return Fraction(collect_fractions([self.tuple_fraction, other.tuple_fraction]))

	def __eq__(self, other):
		return self.tuple_fraction == other.tuple_fraction

	def __str__(self):
		return '{nominator}/{denominator}'.format(nominator = self.tuple_fraction[0], denominator = self.tuple_fraction[1])

	def __repr__(self):
		return 'Fraction {fraction}'.format(fraction = self)

	def __lt__(self, other):
		return self.tuple_fraction[0] / self.tuple_fraction[1] < other.tuple_fraction[0] / other.tuple_fraction[1]
