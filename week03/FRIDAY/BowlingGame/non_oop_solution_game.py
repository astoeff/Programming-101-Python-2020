def find_frames(frames):
	frames_count = 0
	result = []
	current_score= -1
	tenth_frame_shots = []
	for el in frames:
		if frames_count == 9:
			tenth_frame_shots.append(el)
		else:
			if el == 10:
				frames_count += 1
				result.append((10,))
			else:
				if current_score != -1:
					result.append((current_score, el))
					current_score = -1
					frames_count += 1
				else:
					current_score += el + 1
	result.append(tuple(tenth_frame_shots))
	return result

def is_strike(frame):
	return len(frame) == 1

def is_spare(frame):
	return frame[0] + frame[1] == 10

def modify_values(frames):
	result = []
	for i in range(len(frames) - 1):
		if is_strike(frames[i]):
			if is_strike(frames[i + 1]):
				result.append(20 + frames[i+2][0])
			else:
				result.append(10 + frames[i+1][0] + frames[i+1][1])
		elif is_spare(frames[i]):
			result.append(frames[i][0] + frames[i][1] + frames[i+1][0])
		else:
			result.append(frames[i][0] + frames[i][1])
	result.append(sum(list(frames[len(frames)-1])))
	return result
			
#total_shots = [1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2]
#total_shots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#total_shots = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
total_shots = [6, 1, 7, 3, 10, 6, 4, 8, 1, 5, 3, 9, 1, 10, 10, 9, 1, 10]
#total_shots = [5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6]
frames = find_frames(total_shots)
print(frames)
print((modify_values(frames)))
print(sum(modify_values(frames)))
