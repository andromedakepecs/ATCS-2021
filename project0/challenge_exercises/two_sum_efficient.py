# More efficient (O(NlogN) vs o(N^2) version of two_sum program)
# Assuming only one solution, find indices of two numbers that add to target

def two_sum(nums, target):
	new_nums = sorted(nums)	# Function with O(nlogn) complexity
	i = 0	# Pointer positioned at first index of list
	j = len(nums) - 1 	# Pointer positioned at last index of list
	
	found = False
	while not found:
		firstn = new_nums[i]
		secondn = new_nums[j]
		if firstn + secondn == target:
			found = True
			return [nums.index(firstn), nums.index(secondn)] # Problem with this program -- repeat indices of old list
		elif firstn + secondn > target:
			j -= 1
		elif firstn + secondn < target:
			i += 1
		else:
			return None





print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))


