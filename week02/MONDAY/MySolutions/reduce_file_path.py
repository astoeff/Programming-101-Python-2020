def reduce_file_path(path):
    path_given = path.split("/")
    result = "/"
    while '' in path_given:
    	path_given.remove('')

    while '.' in path_given:
    	path_given.remove('.')

    last_dir_len = 0
    for i in path_given:
    	res_len = len(result)
    	if i == "..":
    		result = result[:res_len - last_dir_len-1]
    	else:
    		last_dir_len = len(i)
    		result += i
    		result += '/'

    if result == "":
    	result = "/"

    if result != "/":
    	result = result[:len(result) - 1]

    print(result)


def main():
	reduce_file_path("/")
	reduce_file_path("/srv/../")
	reduce_file_path("/srv/www/htdocs/wtf/")
	reduce_file_path("/srv/www/htdocs/wtf")
	reduce_file_path("/srv/./././././")
	reduce_file_path("/etc//wtf/")
	reduce_file_path("/etc/../etc/../etc/../")
	reduce_file_path("//////////////")
	reduce_file_path("/../")

if __name__ == '__main__':
	main()