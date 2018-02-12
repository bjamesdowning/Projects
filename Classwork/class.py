import words as wds
import string

#Print all letters that never appear doubled

vowels = 'aeiou'
def has_all_vowels(word):
	for vowel in vowels:
		if vowel not in word:
			return False
	return True

for word in wds.wordlist:
	if has_all_vowels(word):
		print(word)
	

