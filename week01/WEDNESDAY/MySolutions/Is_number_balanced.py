def find_left_sum(str, mid):
	return sum([int(i) for i in str[0:mid]])

def find_right_sum(str,mid):
	return sum([int(i) for i in str[mid:]])


def is_number_balanced(n):
	number_in_string = str(n)
	length = len(number_in_string)
	mid = length // 2 
	sum_left = 0
	sum_right = 0
	if length % 2 == 0:
		sum_left = find_left_sum(number_in_string,mid)
		sum_right = find_right_sum(number_in_string,mid)
	else:
		sum_left = find_left_sum(number_in_string,mid)
		sum_right = find_right_sum(number_in_string,mid+1)
	
	return sum_left == sum_right	

print(is_number_balanced(9))
print(is_number_balanced(4518))
print(is_number_balanced(28471))
print(is_number_balanced(1238033))
