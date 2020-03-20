import re

def sum_of_numbers(input_string):
    return sum([(int)(i) for i in re.split(r'[^0-9]',input_string) if i != ''])

print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
print(sum_of_numbers("ab"))
print(sum_of_numbers("1101"))
print(sum_of_numbers("1111O"))
print(sum_of_numbers("1abc33xyz22"))
print(sum_of_numbers("0hfabnek"))