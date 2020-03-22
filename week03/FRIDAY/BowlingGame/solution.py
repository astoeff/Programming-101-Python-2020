class Frame:
	def __init__(self, shots):
		self.__shots = shots

	def get_shots(self):
		return self.__shots

	def is_strike(self):
		return len(self.__shots) == 1

	def is_spare(self):
		if len(self.__shots ) == 2:
			return self.__shots[0] + self.__shots[1] == 10
		return False

	def calculate_value(self):
		return sum(list(self.__shots))

	def __eq__(self, other):
		return self.__shots == other.get_shots()

class BowlingGame:
	def find_frames(total_shots):
		frames_count = 0
		frames = []
		current_score= -1
		tenth_frame_shots = []
		for shot in total_shots:
			if frames_count == 9:
				tenth_frame_shots.append(shot)
			else:
				if shot == 10:
					frames_count += 1
					frames.append(Frame((10,)))
				else:
					if current_score != -1:
						frames.append(Frame((current_score, shot)))
						current_score = -1
						frames_count += 1
					else:
						current_score += shot + 1
		if tenth_frame_shots != []:
			frames.append(Frame(tuple(tenth_frame_shots)))
		return frames

	def validate_frames(frames):
		if len(frames) == 10:
			if len(frames[9].get_shots()) == 2:
				if sum(list(frames[9].get_shots())) < 10:
					return True
				else:
					return False
			elif len(frames[9].get_shots()) == 3:
				if sum(list(frames[9].get_shots()[:2])) >= 10:
					return True
				else:
					return False
			return False
		return False

	def __init__(self, total_shots):
		frames = BowlingGame.find_frames(total_shots)
		if BowlingGame.validate_frames(frames):
			self.__frames = frames
		else:
			raise ValueError('Invalid shots for a game given')

	def get_frames(self):
		return self.__frames

	def calculate_frames_values(self):
		frames_values = []
		for i in range(len(self.__frames) - 1):
			if self.__frames[i].is_strike():
				if self.__frames[i + 1].is_strike():
					frames_values.append(20 + self.__frames[i+2].get_shots()[0])
				else:
					frames_values.append(10 + self.__frames[i+1].get_shots()[0] + self.__frames[i+1].get_shots()[1])
			elif self.__frames[i].is_spare():
				frames_values.append(self.__frames[i].get_shots()[0] + self.__frames[i].get_shots()[1] + self.__frames[i+1].get_shots()[0])
			else:
				frames_values.append(self.__frames[i].get_shots()[0] + self.__frames[i].get_shots()[1])
		frames_values.append(sum(list(self.__frames[len(self.__frames)-1].get_shots())))
		return frames_values


	def calculate_game_score(self):
		return sum(self.calculate_frames_values())