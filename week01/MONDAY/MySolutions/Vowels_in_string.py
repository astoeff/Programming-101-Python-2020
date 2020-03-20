def count_vowels(str):
    str_lower = str.lower()
    vowels = "aeiouy"
    count = 0
    for x in str_lower:
        if x in vowels:
            count+=1
    return count

print(count_vowels("A nice day to code!"))
