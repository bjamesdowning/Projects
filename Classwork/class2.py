import words as wds

'''
Test comment
'''

longest = ''

for word in wds.wordlist:
	if word == word[::-1] and len(word) >= len(longest):
		longest = word
print(longest)


