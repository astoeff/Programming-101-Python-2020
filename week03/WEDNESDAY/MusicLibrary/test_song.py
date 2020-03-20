import unittest
from song import Song



#Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

class TestValidateLength(unittest.TestCase):
	def test_with_given_length_containing_invalid_symbol_should_return_false(self):
		length = 'a3:40'

		result = Song.validate_length(length)

		self.assertEqual(result, False)

	# def test_with_given_length_containing_only__should_return_false(self):
	# 	length = 'a3:40'

	# 	result = Song.validate_length(length)

	# 	self.assertEqual(result, False)

class TestValidateArguments(unittest.TestCase):
	def test_with_given_invalid_title_should_return_false(self):
		arguments = [None, "artist_name", "album_name", "3:44"]

		result = Song.validate_arguments(arguments[0], arguments[1], arguments[2], arguments[3])

		self.assertEqual(result, False)

	def test_with_given_invalid_artis_should_return_false(self):
		arguments = ["title", 55, "album_name", "3:44"]

		result = Song.validate_arguments(arguments[0], arguments[1], arguments[2], arguments[3])

		self.assertEqual(result, False)

	def test_with_given_invalid_album_should_return_false(self):
		arguments = ["title", "artist_name", ["album_name"], "3:44"]

		result = Song.validate_arguments(arguments[0], arguments[1], arguments[2], arguments[3])

		self.assertEqual(result, False)

	def test_with_given_invalid_length_string_should_return_false(self):
		arguments = ["title", "artist_name", "album_name", ""]

		result = Song.validate_arguments(arguments[0], arguments[1], arguments[2], arguments[3])

		self.assertEqual(result, False)

	def test_with_given_length_with_invalid_symbols_should_return_false(self):
		arguments = ["title", "artist_name", "album_name", "a3:40"]

		result = Song.validate_arguments(arguments[0], arguments[1], arguments[2], arguments[3])

		self.assertEqual(result, False)

	def test_with_given_valid_arguments_should_return_true(self):
		arguments = ["title", "artist_name", "album_name", "3:40"]

		result = Song.validate_arguments(arguments[0], arguments[1], arguments[2], arguments[3])

		self.assertEqual(result, True)


class TestInitialisation(unittest.TestCase):
	def test_with_invalid_arguments_given_should_raise_exception(self):
		arguments = ["", "artist_name", "album_name", "3:40"]

		exc = None
		try:
			song = Song(arguments[0], arguments[1], arguments[2], arguments[3])
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid arguments given, title, artist, album need to be non-empty strings and length needs to be in format hh:mm:ss')

	def test_with_invalid_arguments_given_should_raise_exception(self):
		arguments = ["title", "artist_name", "album_name", "3:40"]

		song = Song(arguments[0], arguments[1], arguments[2], arguments[3])

		self.assertEqual(type(song), Song)
		self.assertEqual(song.title, arguments[0])
		self.assertEqual(song.artist, arguments[1])
		self.assertEqual(song.album, arguments[2])
		self.assertEqual(song.length, arguments[3])

class TestStringRepresentation(unittest.TestCase):
	def test_with_given_song_should_cast_to_string_correctly(self):
		title = 'Song'
		artist = 'Artist'
		album = 'First album'
		length = '4:20'
		song = Song(title, artist, album, length)

		song_to_string = str(song)
		expected = '{ar} - {t} from {al} - {l}'.format(ar=artist, t=title, al=album, l=length)

		self.assertEqual(song_to_string, expected)

class TestEqualsDunder(unittest.TestCase):
	def test_with_equal_songs_should_return_true(self):
		title = 'Song'
		artist = 'Artist'
		album_one = 'First album'
		length_one = '3:20'
		album_two = 'Second album'
		length_two = '3:50'

		song_one = Song(title, artist, album_one, length_one)
		song_two = Song(title, artist, album_two, length_two)

		self.assertEqual(song_one, song_two)		

	def test_with_non_equal_songs_should_return_false(self):
		title = 'Song'
		artist_one = 'Artist 1'
		artist_two = 'Artist 2'
		album_one = 'First album'
		length_one = '3:20'
		album_two = 'Second album'
		length_two = '3:50'

		song_one = Song(title, artist_one, album_one, length_one)
		song_two = Song(title, artist_two, album_two, length_two)

		self.assertNotEqual(song_one, song_two)	

class TestHashDunder(unittest.TestCase):
	def test_with_valid_song_should_be_hashable(self):
		exc = None
		try:
			songs_dictionary = {Song('Song', 'Artist', 'Album', '3:30') : 1}
		except Exception as e:
			exc = e

		self.assertIsNone(exc)

	def test_with_valid_song_when_already_in_dict_should_replace_the_value(self):
		song_one = Song('Song', 'Artist', 'Album 1', '3:30')
		song_two = Song('Song', 'Artist', 'Album 2', '5:00')
		songs_dictionary = {song_one : 1}
		
		songs_dictionary[song_two] = 2
		expected = {Song('Song', 'Artist', 'Album 1', '3:20') : 2}
		
		self.assertEqual(songs_dictionary, expected)

	def test_with_valid_song_when_not_in_dict_should_add_to_dict(self):
		song_one = Song('Song 1', 'Artist', 'Album 1', '3:30')
		song_two = Song('Song 2', 'Artist', 'Album 1', '3:30')
		songs_dictionary = {song_one : 1}
		
		songs_dictionary[song_two] = 2
		expected = {song_one : 1, song_two : 2}
		
		self.assertEqual(songs_dictionary, expected)




if __name__ == '__main__':
	unittest.main()