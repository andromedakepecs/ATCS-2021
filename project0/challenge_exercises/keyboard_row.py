# Test cases
words1 = ['hello', 'alaska', 'dad', 'peace']
words2 = ['omk']
words3 = ['adsdf', 'sfd']

# Find words in list that can be typed using letters 
# of the alphabet on only one row of American keyboard
def find_words(words):
	row1 = ['q','w','e','r','t','y','i','o','p']
	row2 = ['a','s','d','f','g','h','j','k','l']
	row3 = ['z','x','c','v','b','n','m']

	one_row_words = []

	for word in words:
		letters_in_rows = [False, False, False]
		for letter in word:
			if letter in row1:
				letters_in_rows[0] = True
			elif letter in row2:
				letters_in_rows[1] = True
			elif letter in row3:
				letters_in_rows[2] = True
		if letters_in_rows.count(True) == 1:
			one_row_words.append(word)

	return one_row_words

print(find_words(words1))
print(find_words(words2))
print(find_words(words3))





