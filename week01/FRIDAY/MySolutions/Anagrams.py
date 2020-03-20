# def is_words_anagram(word1, word2):
# 	word1_to_check = sorted([i for i in word1.lower()])
# 	word2_to_check = sorted([i for i in word2.lower()])
# 	if word1_to_check == word2_to_check:
# 		return 'ANAGRAMS'
# 	return 'NOT ANAGRAMS'



word1 = input('Enter the first word: ')
word2 = input('Enter the second word: ')
#print(is_words_anagram(word1, word2))


print("ANAGRAMS" if sorted([i for i in word1.lower()]) == sorted([i for i in word2.lower()]) else "NOT ANAGRAMS")
