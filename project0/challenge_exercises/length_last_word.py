# Find length of last word in a string
def length_of_last_word(s):
	words = s.split(' ')
	words = list(filter(None, words))
	return len(words[-1])

# Test cases
s1 = 'Hello world'
s2 =  ' fly me  to  the moon '
s3 = 'luffy is still joyboy'

print(length_of_last_word(s1))
print(length_of_last_word(s2))
print(length_of_last_word(s3))