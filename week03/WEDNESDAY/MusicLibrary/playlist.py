from song import Song
import json
import ast 

class Playlist:
	def __init__(self, name, repeat=False, shuffle=False):
		if type(name) == str and name != '' and type(repeat) == bool and type(shuffle) == bool:
			self.__name = name
			self.__repeat = repeat
			self.__shuffle = shuffle
			self.__songs = []
		else:
			raise ValueError('Invalid argument given, name needs to be non-empty string, repeat and shuffle are optional and are of type bool')

	def get_name(self):
		return self.__name

	def get_repeat(self):
		return self.__repeat

	def get_shuffle(self):
		return self.__shuffle

	def get_songs(self):
		return self.__songs

	def add_song(self, song):
		if type(song) == Song:
			if song not in self.__songs:
				self.__songs.append(song)
		else:
			raise TypeError('Argument not a Song')

	def add_songs(self, songs):
		if type(songs) == list:
			for song in songs:
				try:
					self.add_song(song)
				except Exception:
					pass
		else:
			raise TypeError('Argument not a list')

	def remove_song(self, song):
		if type(song) == Song:
			if song not in self.__songs:
				pass
			else:
				self.__songs.remove(song)
		else:
			raise TypeError('Argument not a Song')

	def save(self):
		with open('{name}.json'.format(name=self.__name.replace(' ', '-')), 'w') as f:
			for i in self.__songs:
				json.dump(i.toJSON(), f)
				json.dump('\n', f)

	def toJSON(self):
		return json.dumps(self.__dict__)

	@classmethod
	def load(cls, path):
		with open(path, 'r') as f:
			return json.load(f)
	# print(my_object)
	# print(type(my_object))

class Payload:
	 def __init__(self, j):
		 self.__dict__ = json.loads(j)

def main():
	playlist = Playlist('first playlist made')
	playlist.add_song(Song('song', 'album', 'artist', '3:20'))
	playlist.add_song(Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44"))
	print(playlist.toJSON())
	# playlist.save()

	playlist = Playlist('name')
	# p = Payload()
	# # songs = ast.literal_eval(Playlist.load('first-playlist-made.json')) 
	# #songs = [Song(dict(i)['title'], dict(i)['artist'] ,dict(i)['album'], dict(i)['length']) for i in )]
	# print(songs)
	# # playlist.add_songs(songs)
	# # print(playlist.__dict__)


if __name__ == '__main__':
	main()