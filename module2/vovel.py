def isVowel(ch):
	switcher = {
		'a': "Vowel",
		'e': "Vowel",
		'i': "Vowel",
		'o': "Vowel",
		'u': "Vowel",
		'A': "Vowel",
		'E': "Vowel",
		'I': "Vowel",
		'O': "Vowel",
		'U': "Vowel"
	}
	return switcher.get(ch, "Consonant")

# Driver Code
print('a is '+isVowel('a'))
print('x is '+isVowel('x'))
