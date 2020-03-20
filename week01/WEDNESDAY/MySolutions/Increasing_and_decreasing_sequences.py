def increasing_or_decreasing(seq):
    seq_to_set = set(seq)
    if sorted(seq) == sorted(list(seq_to_set)):
    	if seq == sorted(seq):
    		return 'Up!'
    	elif seq == sorted(seq, reverse=True):
    		return 'Down!'
    	else:
    		return False
    return False

print(increasing_or_decreasing([1,2,3,4,5]))
print(increasing_or_decreasing([5,6,-10]))
print(increasing_or_decreasing([1,1,1,1]))
print(increasing_or_decreasing([9,8,7,6]))