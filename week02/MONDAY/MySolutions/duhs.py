import sys
import os

def duhs_command(path):
	objects_in_path = []
	total_sum = 0
	try:
		obejcts_in_path = os.listdir(path)
	except Exception as e:
		print("Cannot get what is in ",path, "\nEither no such folder or no permissions!")
	else:
		for i in obejcts_in_path:
			total_sum += int(os.stat(i).st_size)
		print(total_sum, " ", path)

def main():
	if len(sys.argv) != 2:
		print("Invalid number of arguments, you need path as 1st only!")
	else:
		#print(sum(os.path.getsize(f) for f in os.listdir(sys.argv[1])))
		total_sum = 0
		for i in list(os.walk(sys.argv[1])):
			for j in i:
				if os.path.isdir(j):
					pass
				else:
					for z in j:
						print(z)
				#total_sum += int(os.stat(i).st_size)
		print(total_sum) 

		#duhs_command(sys.argv[1])

if __name__ == '__main__':
	main()