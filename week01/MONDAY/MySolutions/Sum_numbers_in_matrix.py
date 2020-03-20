def sum_matrix(m):
	return sum(sum(i) for i in m)

print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))