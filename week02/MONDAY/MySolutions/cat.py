import sys

def cat(arguments):
	try:
		with open(arguments, "r") as f:
			print(f.read())
	except Exception as e:
		print("Invalid name of file: ",sys.argv[1])
	


def main():
	if len(sys.argv) == 2:
		cat(sys.argv[1])
	else:
		print("Invalid number of arguments!")

if __name__ == '__main__':
	main()