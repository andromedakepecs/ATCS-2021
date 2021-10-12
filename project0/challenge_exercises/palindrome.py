import string

# Convert string with any characters into just alphabet
def to_letters(s):
	new_str = ''
	alphabet = list(string.ascii_letters)
	for letter in s:
		if letter in alphabet:
			new_str += letter
	return new_str.lower()

# Determine if s is a palindrome
def valid_palindrome(s):
	s = to_letters(s)
	valid = True
	for i in range(len(s)):
		if s[i] != s[-i-1]:
			valid = False
	return valid

# Test cases
s1 = 'A man, a plan, a canal: Panama'
s2 = 'race a car'

print(valid_palindrome(s1))
print(valid_palindrome(s2))
