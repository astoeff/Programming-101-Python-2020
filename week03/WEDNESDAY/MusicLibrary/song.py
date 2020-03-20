#Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
class Song:
	def validate_length(length):
		allowed_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':']
		for symbol in length:
			if symbol not in allowed_symbols:
				return False
		return True

	def validate_arguments(title, artist, album, length):
		if type(title) != str or type(artist) != str or type(album) != str or type(length) != str:
			return False
		if title == '' or artist == '' or album == '' or length == '':
			return False
		return Song.validate_length(length)


	def __init__(self, title, artist, album, length):
		if Song.validate_arguments(title, artist, album, length):
			self.title = title
			self.artist = artist
			self.album = album
			self.length = length
		else:
			raise ValueError('Invalid arguments given, title, artist, album need to be non-empty strings and length needs to be in format hh:mm:ss')

	def __str__(self):
		return '{ar} - {t} from {al} - {l}'.format(ar=self.artist, t=self.title, al=self.album, l=self.length)

	def __eq__(self, other):
		return self.title == other.title and self.artist == other.artist

	def __hash__(self):
		return hash(self.title) + hash(self.artist)
	
	def __repr__(self):
		return str(self)

if __name__ == '__main__':
	def func(** kwargs):
		if len(kwargs) == 1:			
			if list(kwargs.keys())[0] == 's':
				return 's'
			if list(kwargs.keys())[0] == 'm':
				return 'm'
			if list(kwargs.keys())[0] == 'h':
				return 'h'
		return 'hh:mm:ss'

	print(func(h=True, s=True))

