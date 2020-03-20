class Playlist:
	def __init__(self, name, repeat=False, shuffle=False):
		if type(name) == str and name != '' and type(repeat) == bool and type(shuffle) == bool:
			pass
		else:
			self.assertEqual(str(exc), 'Invalid argument given, name needs to be non-empty string, repeat and shuffle are optional and are of type bool')
