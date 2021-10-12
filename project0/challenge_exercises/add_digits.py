# Given an integer num, repeatedly add all 
# its digits until the result has only one digit
def add_digits(n):
	nums = []
	if n > 9:
		for digit in str(n):
			nums.append(int(digit))
		n = add_digits(sum(nums))
	return n

# Test cases
print(add_digits(38))
print(add_digits(0))
print(add_digits(382))
print(add_digits(12435))

