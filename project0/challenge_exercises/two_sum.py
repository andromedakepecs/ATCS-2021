# Assuming only one solution, find indices of two numbers that add to target
def two_sum(nums, target):
	two_num = []
	for i in range(len(nums)):
		for j in range(i + 1, len(nums)):
			if nums[i] + nums[j] == target:
				two_num.append(i)
				two_num.append(j)
				break
	return two_num	

# Test cases
nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))

nums = [3,2,4]
target = 6
print(two_sum(nums, target))

nums = [3,3]
target = 6
print(two_sum(nums, target))
