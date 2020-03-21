def count_frames(frames):
	result = 0
	current_score = -1
	for el in frames:
		if result == 9:
			return 10
		if el == 10:
			result += 1
		else:
			if current_score != -1:
				current_score = -1
				result += 1
			else:
				current_score += el + 1
	return result

def find_frames(frames):
	# frames_count = 0
	# result = []
	# current_score = -1
	# tenth_frame_shots = 0
	# for el in frames:
	# 	if frames_count == 9:
	# 		current_score += el
	# 		tenth_frame_shots += 1
	# 	else:
	# 		if el == 10:
	# 			frames_count += 1
	# 			result[el] = 1
	# 		else:
	# 			if current_score != -1:
	# 				result[current_score + el] = 2
	# 				current_score = -1
	# 				frames_count += 1
	# 			else:
	# 				current_score += el + 1
	# result[current_score + 1] = tenth_frame_shots
	# return result

	frames_count = 0
	result = []
	current_score= -1
	current_frame = ()
	tenth_frame_shots = []
	for el in frames:
		if frames_count == 9:
			# current_score += el
			# tenth_frame_shots += 1
			tenth_frame_shots.append(el)
			print(el)
		else:
			if el == 10:
				frames_count += 1
				result.append((10,))
			else:
				if current_score != -1:
					# result[current_score + el] = 2
					result.append((current_score, el))
					current_score = -1
					frames_count += 1
				else:
					current_score += el + 1
	result.append(tuple(tenth_frame_shots))
	return result

def find_strike_and_spare_frames(shots, frames):
	strike_or_spare_position = 0
	indexes_passed = -1
	result = ([], [])
	for el in frames:
		if el == 10:
			if shots[indexes_passed + 1] == 10:
				result[0].append(strike_or_spare_position)
				indexes_passed += 1
			else:
				result[1].append(strike_or_spare_position)
				indexes_passed += 2
		else:
			indexes_passed += 2
		strike_or_spare_position += 1
	return result

def calculate_strike_values(shots, strikes):
	strikes_passed = 0
	result = {}
	for el in strikes:
		result[el] = 10 + shots[el*2 - strikes_passed + 1] + shots[el*2 - strikes_passed + 2]
		strikes_passed += 1
	return result

def calculate_spare_values(shots, spares, strikes):
	strikes_pos = 0
	result = {}
	for el in spares:

		result[el] = 10 + shots[el*2 - strikes_passed + 1] + shots[el*2 - strikes_passed + 2]
		strikes_passed += 1
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
			

			


#def find_strike_positions()
#total_shots = [1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2]
#total_shots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#total_shots = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
total_shots = [6, 1, 7, 3, 10, 6, 4, 8, 1, 5, 3, 9, 1, 10, 10, 9, 1, 10]
#total_shots = [5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6]
frames = find_frames(total_shots)
print(frames)
# strikes = []
# spares = []
# for i in range(len(frames) - 1):
# 	if is_strike(frames[i]):
# 		strikes.append(i)
# 	elif is_spare(frames[i]):
# 		spares.append(i)
# print(strikes)
# print(spares)
print((modify_values(frames)))
print(sum(modify_values(frames)))

# strikes = find_strike_and_spare_frames(total_shots, frames[:(len(frames)-1)])[0]
# spares = find_strike_and_spare_frames(total_shots, frames[:(len(frames)-1)])[1]
# print('Strikes: ', strikes)
# print('Spares: ', spares)
# print(calculate_strike_values(total_shots, strikes))
# total_score = 0
# to_skip = False
# for i in range(len(total_shots)):
# 	if to_skip:
# 		to_skip = False
# 		continue
# 	else:
# 		#print(i)
# 		if i == len(total_shots) -1:
# 			total_score += total_shots[i]
# 			break
# 		else:
# 			if total_shots[i] == 10:					#strike
# 				if total_shots[i + 1] == 10:
# 					if i + 2 == len(total_shots):
# 						total_score += 20
# 					else:
# 						total_score += 20 + total_shots[i+2]
# 				to_skip = False
# 			else:
# 				if total_shots[i + 1] + total_shots[i] == 10:		#spare
# 					if i + 2 == len(total_shots):
# 						total_score += total_shots[i+1] + total_shots[i]
# 					else:
# 						total_score += total_shots[i+1] + total_shots[i] + total_shots[i+2]
# 				else:
# 					total_score += total_shots[i+1] + total_shots[i]
# 				to_skip = True
# 	#print(total_score)
# if total_score >300:
# 	total_score = 300
# print(total_score)

