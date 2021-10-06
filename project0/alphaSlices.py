# create list
first_ten = 'abcdefghij'
alpha = []
for letter in first_ten:
	alpha.append(letter)

first_three = alpha[:3]
mid_three = alpha[4:7]
end = alpha[6:]

print(first_three)
print(mid_three)
print(end)