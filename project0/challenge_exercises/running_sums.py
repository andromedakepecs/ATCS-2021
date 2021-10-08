# Get array of numbers from console
numbers = []
done = False
while not done:
	inp = input('Enter a number. Type \'done\' if done ')
	if inp == 'done':
		break
	try:
		numbers.append(int(inp))
	except:
		print('Not a number')

# Running sum of number array
def running_sums(nums):
	out = []
	total = 0
	for i in range(len(nums)):
		total += nums[i]
		out.append(total)
	return(out)

print(running_sums(numbers))
	
