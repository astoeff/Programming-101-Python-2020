def birthday_ranges(birthdays, ranges):
	result = []
	birthdays_sorted = sorted(birthdays)
	for i in ranges:
		left_boundary = i[0]
		right_boundary = i[1]
		count = 0
		for j in birthdays_sorted:
			if j >= left_boundary and j <= right_boundary:
				count += 1
		result.append(count)
	return result

print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))