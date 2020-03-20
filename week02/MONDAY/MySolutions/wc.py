import sys

def wc(file,argument):
	f = ""
	text = ""
	words = 0
	chars = 0
	lines = 0
	try:
		with open(file, "r") as f:
			text = f.read()
			#print(text.split(" "))
			#print(text.split("\n"))

	except Exception as e:
		print("Cannot open {f} for reading!".format(f = file))
	else:
		pass
		words = len(text.split())
		chars = len(text)
		#lines = len([i for i in text.split("\n") if i != ""])
		lines = text.count("\n")


	if argument == "words":
		print(words)
	elif argument == "chars":
		print(chars)
	elif argument == "lines":
		print(lines)
	else:
		print("Wrong argument")


def main():
	if len(sys.argv) != 3:
		print("Invalid number of arguments, you a file as 1st argument and  words, chars or lines as 2nd!")
	else:
		wc(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
	main()