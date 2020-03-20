def contains_word(word, text):
	in_text = word in ''.join(text)
	in_text_reversed = word in ''.join(reversed(tex))
	return in_text or in_text_reversed

def word_counter():
	word = input('Enter word: ')
	size = input('Enter matrix size (format NxM): ')

	n=int(size.split(' ')[0])
	m=int(size.split(' ')[1])

	if len(word) > min([n,m]):
		return 'Invalid number of rows or columns'

	matrix = []
	rows_inputted = 0
	print('Enter matrix:')
	while rows_inputted < n:
		row_input = input()
		row = row_input.strip().split(' ')

		if len(row) != m:
			return 'Wrong input'

		matrix.append(row)
		rows_inputted += 1

	word_occurances = 0
	for row in matrix:
		word_occurances += contains_word(word, row):

	for i in range(m):
		column = []
		for row in matrix:
			column.append(row[i])
		word_occurances += contains_word(word, column):
		
	return word_occurances

print(word_counter())