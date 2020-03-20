def count_consonants(str):
    str_lower=str.lower()
    consonants="bcdfghjklmnpqrstvwxz"
    count=0
    for x in str_lower:
    	for y in consonants:
    		if x == y:
    			count+=1
    		else:
    			pass
    return count

print(count_consonants("A nice day to code!"))