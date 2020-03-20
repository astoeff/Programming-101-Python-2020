def char_histogram(string):
    histogram = {}
    for x in string:
    	if x in histogram:
    		histogram[x] += 1
    	else:
    		histogram[x] = 1
    return histogram

print(char_histogram("Python!"))