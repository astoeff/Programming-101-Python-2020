import unittest
from playlist import Playlist
from song import Song

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

	def test_with_given_valid_name_as_only_argument_should_create_instance(self):
		name = 'playlist'

		playlist = Playlist(name)
		
		self.assertEqual(type(playlist), Playlist)
		self.assertEqual(playlist.get_name(), name)
		self.assertEqual(playlist.get_repeat(), False)
		self.assertEqual(playlist.get_shuffle(), False)

	def test_with_given_valid_name_and_repeat_true_as_arguments_should_create_instance(self):
		name = 'playlist'
		repeat = True

		playlist = Playlist(name, repeat)
		
		self.assertEqual(type(playlist), Playlist)
		self.assertEqual(playlist.get_name(), name)
		self.assertEqual(playlist.get_repeat(), repeat)
		self.assertEqual(playlist.get_shuffle(), False)

	def test_with_given_valid_name_repeat_true_and_shuffle_true_as_arguments_should_create_instance(self):
		name = 'playlist'
		repeat = True
		shuffle = True

		playlist = Playlist(name, repeat, shuffle)
		
		self.assertEqual(type(playlist), Playlist)
		self.assertEqual(playlist.get_name(), name)
		self.assertEqual(playlist.get_repeat(), repeat)
		self.assertEqual(playlist.get_shuffle(), shuffle)


class TestAddSong(unittest.TestCase):
	def test_with_given_empyty_playlist_and_song_should_add_song_to_playlist(self):
		playlist = Playlist('playlist')
		song = Song('song', 'album', 'artist', '3:20')

		playlist.add_song(song)

		self.assertEqual(playlist.get_songs(), [song])

	def test_with_given_non_empyty_playlist_and_song_not_in_playlist_should_add_song_to_playlist(self):
		playlist = Playlist('playlist')
		song = Song('song', 'album', 'artist', '3:20')
		song_to_add = Song('New song', 'album', 'artist', '3:20')

		playlist.add_song(song)
		playlist.add_song(song_to_add)

		self.assertEqual(playlist.get_songs(), [song, song_to_add])

	def test_with_given_non_empyty_playlist_and_song_in_playlist_should_do_nothing(self):
		playlist = Playlist('playlist')
		song = Song('song', 'album', 'artist', '3:20')

		playlist.add_song(song)

		playlist.add_song(song)
		
		self.assertEqual(playlist.get_songs(), [song])

	def test_with_given_playlist_and_not_a_song_should_raise_exception(self):
		playlist = Playlist('playlist')
		song = Song('song', 'album', 'artist', '3:20')

		playlist.add_song(song)

		exc = None
		try:
			playlist.add_song('song')
		except Exception as e:
			exc = e 

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Argument not a Song')

class TestRemoveSong(unittest.TestCase):
	def test_with_given_empty_list_and_song_should_do_nothing(self):
		playlist = Playlist('playlist')
		song = Song('song', 'album', 'artist', '3:20')

		playlist.remove_song(song)

		self.assertEqual(playlist.get_songs(), [])

	def test_with_given_non_empty_list_and_song_not_in_list_should_do_nothing(self):
		playlist = Playlist('playlist')
		song = Song('song', 'album', 'artist', '3:20')
		playlist.add_song(song)
		song_to_remove = Song('remove me', 'album', 'artist', '3:20')

		playlist.remove_song(song_to_remove)

		self.assertEqual(playlist.get_songs(), [song])

	def test_with_given_non_empty_list_and_song_in_list_should_remove_song(self):
		playlist = Playlist('playlist')
		song = Song('song', 'album', 'artist', '3:20')
		playlist.add_song(song)
		song_to_remove = Song('remove me', 'album', 'artist', '3:20')
		playlist.add_song(song_to_remove)

		playlist.remove_song(song_to_remove)

		self.assertEqual(playlist.get_songs(), [song])

	def test_with_given_list_and_non_song_argument_should_raise_exception(self):
		playlist = Playlist('playlist')
		song = Song('song', 'album', 'artist', '3:20')
		playlist.add_song(song)

		exc = None
		try:
			playlist.remove_song(None)
		except Exception as e:
			exc = e 

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Argument not a Song')

class TestAddSongs(unittest.TestCase):
	def test_with_given_empyty_playlist_and_songs_should_add_songs_to_playlist(self):
		playlist = Playlist('playlist')
		songs = [Song('one', 'album', 'artist', '3:20'), Song('two', 'album', 'artist', '3:20'), Song('three', 'album', 'artist', '3:20')]


		playlist.add_songs(songs)

		self.assertEqual(playlist.get_songs(), songs)

	def test_with_given_non_empyty_playlist_and_all_songs_not_in_list_should_add_songs_to_playlist(self):
		playlist = Playlist('playlist')
		song = Song('song', 'album', 'artist', '3:50')
		playlist.add_song(song)
		songs = [Song('one', 'album', 'artist', '3:20'), Song('two', 'album', 'artist', '3:20'), Song('three', 'album', 'artist', '3:20')]


		playlist.add_songs(songs)

		self.assertEqual(playlist.get_songs(), [song] + songs)

	def test_with_given_non_empyty_playlist_and_one_or_more_songs_in_list_already_should_add_new_songs_to_playlist(self):
		playlist = Playlist('playlist')
		song = Song('song', 'album', 'artist', '3:50')
		playlist.add_song(song)
		one = Song('one', 'album', 'artist', '3:20')
		two =  Song('two', 'album', 'artist', '3:20')
		songs = [song, one, two]

		playlist.add_songs(songs)

		self.assertEqual(playlist.get_songs(), [song] + [one, two])


	def test_with_given_playlist_and_non_list_should_raise_exception(self):
		playlist = Playlist('playlist')
		song = Song('song', 'album', 'artist', '3:50')
		playlist.add_song(song)
		one = Song('one', 'album', 'artist', '3:20')
		two =  Song('two', 'album', 'artist', '3:20')
		songs = (one, two)

		exc = None 
		try:
			playlist.add_songs(songs)
		except Exception as e:
			exc = e 

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Argument not a list')

	def test_with_given_playlist_and_list_with_one_or_more_elements_not_song_should_pass_them(self):
		playlist = Playlist('playlist')
		song = Song('song', 'album', 'artist', '3:50')
		playlist.add_song(song)
		one = Song('one', 'album', 'artist', '3:20')
		two =  Song('two', 'album', 'artist', '3:20')
		three = Song('three', 'album', 'artist', '3:20')
		songs = [one, [three] ,two ]

		playlist.add_songs(songs)
		
		self.assertEqual(playlist.get_songs(), [song, one, two])


if __name__ == '__main__':
	
	unittest.main()