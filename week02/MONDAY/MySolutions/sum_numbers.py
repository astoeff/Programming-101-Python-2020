import sys

def sum_numbers(filename):
	numbers = []
	f = ""
	try:
		with open(filename, "r") as f:
			pass
	except Exception as e:
		print("Cannot open {file} for reading!".format(file = filename))
	else:
		with open(filename, "r") as f:
			tokens = f.read().split(" ")		
		try:
			numbers = [int(i) for i in tokens]
		except Exception:
			print("The file contains not only numbers!")
		else:
			print(sum(numbers))
	finally:
		pass


def main():
	if len(sys.argv) != 2:
		print("Invalid number of arguments, you need file as 1st only!")
	else:
		sum_numbers(sys.argv[1])

if __name__ == '__main__':
	main()