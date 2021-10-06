try:
	num1 = int(input("Enter number: "))
	num2 = int(input("Enter number: "))
except:
	print('Not a number')
	exit()

def add_num(num1, num2):
	sum = num1 + num2
	return sum

print(num1, '+', num2, '=', add_num(num1, num2))



