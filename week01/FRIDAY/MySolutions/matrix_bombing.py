def is_position_in_matrix(i,j,n,m):
	return i >= 0 and i<n and j>=0 and j<m 

def make_negative_numbers_zero(n):
	return n if n >= 0 else 0

def print_matrix(m):
	for row in m:
		for el in row:
			print(el,end = " ")
		print()

def matrix_bombing_plan(m):
	size_n = len(m)
	size_m = len(m[0])
	i = 0
	j = 0
	matrix_modified_for_el = [[el for el in row] for row in m]
	result = {}
	for row in m:
		j = 0
		for el in row:			
			matrix_modified_for_el = [[el for el in row] for row in m]

			if is_position_in_matrix(i - 1, j - 1, size_n, size_m):
				matrix_modified_for_el[i - 1][j - 1] -= matrix_modified_for_el[i][j]
				matrix_modified_for_el[i - 1][j - 1] = make_negative_numbers_zero(matrix_modified_for_el[i - 1][j - 1])

			if is_position_in_matrix(i - 1,j,size_n,size_m):
				matrix_modified_for_el[i - 1][j] -= m[i][j]
				matrix_modified_for_el[i - 1][j] = make_negative_numbers_zero(matrix_modified_for_el[i - 1][j])

			if is_position_in_matrix(i - 1, j + 1, size_n, size_m):
				matrix_modified_for_el[i - 1][j + 1] -= m[i][j]
				matrix_modified_for_el[i - 1][j + 1] = make_negative_numbers_zero(matrix_modified_for_el[i - 1][j + 1])

			if is_position_in_matrix(i,j - 1,size_n,size_m):
				matrix_modified_for_el[i][j - 1] -= m[i][j]
				matrix_modified_for_el[i][j - 1] = make_negative_numbers_zero(matrix_modified_for_el[i][j - 1])

			if is_position_in_matrix(i,j + 1,size_n,size_m):
				matrix_modified_for_el[i][j + 1] -= m[i][j]
				matrix_modified_for_el[i][j + 1] = make_negative_numbers_zero(matrix_modified_for_el[i][j + 1])

			if is_position_in_matrix(i + 1,j - 1,size_n,size_m):
				matrix_modified_for_el[i + 1][j - 1] -= m[i][j]
				matrix_modified_for_el[i + 1][j - 1] = make_negative_numbers_zero(matrix_modified_for_el[i + 1][j - 1])

			if is_position_in_matrix(i + 1,j,size_n,size_m):
				matrix_modified_for_el[i + 1][j] -= m[i][j]
				matrix_modified_for_el[i + 1][j] = make_negative_numbers_zero(matrix_modified_for_el[i + 1][j])

			if is_position_in_matrix(i + 1,j + 1,size_n,size_m):
				matrix_modified_for_el[i + 1][j + 1] -= m[i][j]
				matrix_modified_for_el[i + 1][j + 1] = make_negative_numbers_zero(matrix_modified_for_el[i + 1][j + 1])

			result[(i,j)] = sum(sum(row) for row in matrix_modified_for_el)
			j += 1
		i += 1	
	return result


input_size = ""
iput_n = ""
input_m = ""
while True:
	try:
		input_size = input("Enter size of matrix in format NxM: ")
		size = input_size.split("x")
		input_n = size[0]
		input_m = size[1]
		n = int(input_n)
		m = int(input_m)
	except Exception as e:
		print("Wrong input!")
	else:
		break

print("{n}x{m}".format(n=input_n,m=input_m))
print("Enter your matrix, each element on new line!")

matrix = []
for i in range(n):
	row = []
	print("Enter row: ")
	for j in range(m):
		matrix_element = input()
		row.append(int(matrix_element))
	matrix.append(row)

print("You entered: ")
print_matrix(matrix)

print(matrix_bombing_plan(matrix))