import sys
from cat import cat


def cat2(arguments):
	for i in arguments:
		cat(i)
		print()


def main():
	if len(sys.argv) > 1:
		cat2(sys.argv[1:])
	else:
		print("No file given for reading!")

if __name__ == '__main__':
	main()