def is_credit_card_valid(number):
	number_in_string = str(number)
	if len(number_in_string) % 2 == 1:
		even_pos_digits = number_in_string[::2]
		odd_pos_digits = number_in_string[1::2]
		odd_pos_digits_transformed_list = [int(i)*2 for i in odd_pos_digits]
		odd_pos_digits_transfored_string = "".join(str(i) for i in odd_pos_digits_transformed_list)
		sum_digits = sum([int(i) for i in odd_pos_digits_transfored_string + even_pos_digits])
		print(sum_digits)
		if sum_digits % 10 == 0:
			return True
	return False

print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))
