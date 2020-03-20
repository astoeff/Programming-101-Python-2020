# generate_numbers.py
import sys
from random import randint
import os.path
from os import path



def generate_numbers(filename, numbers):
	if path.exists(str(filename)):
			print("A file with name {file} already exists!".format(file = str(filename)))
	else:
		try:
			numbers_range = int(numbers)
		except Exception:
			print("2nd argument need to be a number!")
			return 
		try:
			with open(filename, "w") as f:
				for i in range(int(numbers)-1):
					f.write(str(randint(1,1000)))
					f.write(" ")
				f.write(str(randint(1,1000)))				
		except Exception as e:
			print(e)
			print("Problem with opening file: ", filename, " or writing in it!")
		


def main():
	if len(sys.argv) != 3:
		print("Invalid number of arguments, you need file as 1st argument and integer as 2nd argument!")
	else:
		generate_numbers(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
	main()