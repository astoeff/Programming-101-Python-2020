import unittest
from playlist import Playlist

class TestInitialisation(unittest.TestCase):
	def test_with_given_non_string_name_should_raise_exception(self):
		name = None

		exc = None
		try:
			playlist = Playlist(name)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid argument given, name needs to be non-empty string, repeat and shuffle are optional and are of type bool')


if __name__ == '__main__':
	
	unittest.main()