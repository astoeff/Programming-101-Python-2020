import unittest
from game import Frame

class TestInitialisation(unittest.TestCase):
	def test_with_given_spare_should_create_instance(self):
		shots = (1, 9)

		frame = Frame(shots)
		expected_shots = shots

		self.assertEqual(type(frame), Frame)
		self.assertEqual(frame.get_shots(), expected_shots)

	def test_with_given_strike_should_create_instance(self):
		shots = (10,)

		frame = Frame(shots)
		expected_shots = shots

		self.assertEqual(type(frame), Frame)
		self.assertEqual(frame.get_shots(), expected_shots)

	def test_with_given_open_frame_should_create_instance(self):
		shots = (0, 0)

		frame = Frame(shots)
		expected_shots = shots

		self.assertEqual(type(frame), Frame)
		self.assertEqual(frame.get_shots(), expected_shots)

	def test_with_given_tenth_frame_should_create_instance(self):
		shots = (10, 10, 10)

		frame = Frame(shots)
		expected_shots = shots

		self.assertEqual(type(frame), Frame)
		self.assertEqual(frame.get_shots(), expected_shots)

class TestIsStrike(unittest.TestCase):
	def test_with_given_strike_should_return_true(self):
		frame = Frame((10,))

		result = frame.is_strike()

		self.assertEqual(result, True)

	def test_with_given_spare_should_return_false(self):
		frame = Frame((5, 5))

		result = frame.is_strike()

		self.assertEqual(result, False)

	def test_with_given_open_frame_should_return_false(self):
		frame = Frame((0, 2))

		result = frame.is_strike()

		self.assertEqual(result, False)

	def test_with_given_tenth_frame_should_return_false(self):
		frame = Frame((10, 10, 10))

		result = frame.is_strike()

		self.assertEqual(result, False)

class TestIsSpare(unittest.TestCase):
	def test_with_given_spare_should_return_true(self):
		frame = Frame((9, 1))

		result = frame.is_spare()

		self.assertEqual(result, True)

	def test_with_given_strike_should_return_false(self):
		frame = Frame((10,))

		result = frame.is_spare()

		self.assertEqual(result, False)

	def test_with_given_open_frame_should_return_false(self):
		frame = Frame((0, 9))

		result = frame.is_spare()

		self.assertEqual(result, False)

	def test_with_given_tenth_frame_should_return_false(self):
		frame = Frame((9, 1, 10))

		result = frame.is_spare()

		self.assertEqual(result, False)

class TestCalculateValues(unittest.TestCase):
	def test_with_given_strike_should_return_10(self):
		frame = Frame((10,))

		result = frame.calculate_value()
		expected = 10

		self.assertEqual(result, expected)

	def test_with_given_spare_should_return_10(self):
		frame = Frame((9, 1))

		result = frame.calculate_value()
		expected = 10

		self.assertEqual(result, expected)

	def test_with_given_open_frame_should_return_correct_value(self):
		frame = Frame((0, 9))

		result = frame.calculate_value()
		expected = 9

		self.assertEqual(result, expected)

	def test_with_given_tenth_frame_spare_and_strike_should_return_20(self):
		frame = Frame((9, 1, 10))

		result = frame.calculate_value()
		expected = 20

		self.assertEqual(result, expected)

	def test_with_given_tenth_frame_spare_and_non_strike_should_return_correct_value(self):
		frame = Frame((9, 1, 5))

		result = frame.calculate_value()
		expected = 15

		self.assertEqual(result, expected)

	def test_with_given_tenth_frame_triple_stike_should_return_30(self):
		frame = Frame((10, 10, 10))

		result = frame.calculate_value()
		expected = 30

		self.assertEqual(result, expected)

	def test_with_given_tenth_frame_double_stike_and_non_strike_should_return_correct_value(self):
		frame = Frame((10, 10, 9))

		result = frame.calculate_value()
		expected = 29

		self.assertEqual(result, expected)

	def test_with_given_tenth_frame_stike_and_non_strike_or_open_frame_should_return_correct_value(self):
		frame = Frame((10, 5, 0))

		result = frame.calculate_value()
		expected = 15

		self.assertEqual(result, expected)

	def test_with_given_tenth_frame_non_stike_and_non_spare_should_return_correct_value(self):
		frame = Frame((2, 0))

		result = frame.calculate_value()
		expected = 2

		self.assertEqual(result, expected)



if __name__ == '__main__':
	unittest.main()

