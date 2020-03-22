import unittest
from game import BowlingGame, Frame

class TestFindFrames(unittest.TestCase):
	def test_with_given_game_should_return_correct_frames_list(self):
		total_shots = [1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2]

		frames = BowlingGame.find_frames(total_shots)
		expected = [Frame((1, 4)), Frame((4, 5)), Frame((6, 3)), Frame((5, 1)), Frame((1, 0)), Frame((1, 7)), Frame((3, 6)), Frame((4, 3)), Frame((2, 1)), Frame((6, 2))]

		self.assertEqual(frames, expected)

	def test_with_given_empty_game_should_return_correct_frames_list(self):
		total_shots = []

		frames = BowlingGame.find_frames(total_shots)
		expected = []

		self.assertEqual(frames, expected)

class TestValidateFrames(unittest.TestCase):
	def test_with_given_less_than_10_frames_should_return_false(self):
		frames = [Frame((1, 4)), Frame((4, 5)), Frame((6, 3)), Frame((5, 1)), Frame((1, 0)), Frame((1, 7)), Frame((3, 6)), Frame((4, 3)), Frame((2, 1))]

		result = BowlingGame.validate_frames(frames)

		self.assertEqual(result, False)

	def test_with_given_10_frames_but_tenth_is_with_zero_shots_should_return_false(self):
		frames = [Frame((1, 4)), Frame((4, 5)), Frame((6, 3)), Frame((5, 1)), Frame((1, 0)), Frame((1, 7)), Frame((3, 6)), Frame((4, 3)), Frame((2, 1)), Frame(())]

		result = BowlingGame.validate_frames(frames)

		self.assertEqual(result, False)

	def test_with_given_10_frames_but_tenth_is_with_one_shot_should_return_false(self):
		frames = [Frame((1, 4)), Frame((4, 5)), Frame((6, 3)), Frame((5, 1)), Frame((1, 0)), Frame((1, 7)), Frame((3, 6)), Frame((4, 3)), Frame((2, 1)), Frame((1,))]

		result = BowlingGame.validate_frames(frames)

		self.assertEqual(result, False)

	def test_with_given_10_frames_and_tenth_is_with_two_shots_and_stike_in_them_should_return_false(self):
		frames = [Frame((1, 4)), Frame((4, 5)), Frame((6, 3)), Frame((5, 1)), Frame((1, 0)), Frame((1, 7)), Frame((3, 6)), Frame((4, 3)), Frame((2, 1)), Frame((10, 2))]

		result = BowlingGame.validate_frames(frames)

		self.assertEqual(result, False)

	def test_with_given_10_frames_and_tenth_is_with_two_shots_and_spare_in_them_should_return_false(self):
		frames = [Frame((1, 4)), Frame((4, 5)), Frame((6, 3)), Frame((5, 1)), Frame((1, 0)), Frame((1, 7)), Frame((3, 6)), Frame((4, 3)), Frame((2, 1)), Frame((1, 9))]

		result = BowlingGame.validate_frames(frames)

		self.assertEqual(result, False)

	def test_with_given_10_frames_and_tenth_is_with_two_shots_and_two_strikes_should_return_false(self):
		frames = [Frame((1, 4)), Frame((4, 5)), Frame((6, 3)), Frame((5, 1)), Frame((1, 0)), Frame((1, 7)), Frame((3, 6)), Frame((4, 3)), Frame((2, 1)), Frame((10, 10))]

		result = BowlingGame.validate_frames(frames)

		self.assertEqual(result, False)

	def test_with_given_10_frames_and_tenth_is_with_two_shots_and_not_spare_or_stike_should_return_true(self):
		frames = [Frame((1, 4)), Frame((4, 5)), Frame((6, 3)), Frame((5, 1)), Frame((1, 0)), Frame((1, 7)), Frame((3, 6)), Frame((4, 3)), Frame((2, 1)), Frame((1,  2))]

		result = BowlingGame.validate_frames(frames)

		self.assertEqual(result, True)

	def test_with_given_10_frames_and_tenth_is_with_three_shots_and_a_spare_in_them_should_return_true(self):
		frames = [Frame((1, 4)), Frame((4, 5)), Frame((6, 3)), Frame((5, 1)), Frame((1, 0)), Frame((1, 7)), Frame((3, 6)), Frame((4, 3)), Frame((2, 1)), Frame((1, 9, 10))]

		result = BowlingGame.validate_frames(frames)

		self.assertEqual(result, True)

	def test_with_given_10_frames_and_tenth_is_with_three_shots_and_a_strike_in_them_should_return_true(self):
		frames = [Frame((1, 4)), Frame((4, 5)), Frame((6, 3)), Frame((5, 1)), Frame((1, 0)), Frame((1, 7)), Frame((3, 6)), Frame((4, 3)), Frame((2, 1)), Frame((10, 10, 2))]

		result = BowlingGame.validate_frames(frames)

		self.assertEqual(result, True)

	def test_with_given_10_frames_and_tenth_is_with_three_shots_and_not_a_spare_or_a_strike_in_them_should_return_false(self):
		frames = [Frame((1, 4)), Frame((4, 5)), Frame((6, 3)), Frame((5, 1)), Frame((1, 0)), Frame((1, 7)), Frame((3, 6)), Frame((4, 3)), Frame((2, 1)), Frame((1, 5, 10))]

		result = BowlingGame.validate_frames(frames)

		self.assertEqual(result, False)

class TestInitialising(unittest.TestCase):
	def test_with_given_correct_game_should_create_instance(self):
		total_shots = [1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2]
		frames_expected =  [Frame((1, 4)), Frame((4, 5)), Frame((6, 3)), Frame((5, 1)), Frame((1, 0)), Frame((1, 7)), Frame((3, 6)), Frame((4, 3)), Frame((2, 1)), Frame((6, 2))]
		
		game = BowlingGame(total_shots)
		
		self.assertEqual(type(game), BowlingGame)
		self.assertEqual(game.get_frames(), frames_expected)

	def test_with_given_incorrect_game_should_raise_exception(self):
		total_shots = [1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1]

		exc = None
		try:
			game = BowlingGame(total_shots)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid shots for a game given')

class TestCalculateFramesValues(unittest.TestCase):
	def test_with_given_game_should_calculate_correctly(self):
		total_shots = [1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2]

		game = BowlingGame(total_shots)
		values = game.calculate_frames_values()
		expected = [5, 9, 9, 6, 1, 8, 9, 7, 3, 8]

		self.assertEqual(values, expected)

class TestCalculateGameScore(unittest.TestCase):
	def test_with_given_game_should_calculate_correctly(self):
		total_shots = [1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2]

		game = BowlingGame(total_shots)
		score = game.calculate_game_score()
		expected = 65

		self.assertEqual(score, expected)


if __name__ == '__main__':
	unittest.main()