# Given an integer numRows, return the first numRows of Pascal's triangle.
# Return list of lists
def generate(num_rows, n1, n2):
	if num_rows == 1:
		return [1]
	else:
		return generate(num_rows)
		



	# if n = 1 list = [1]
	# list size pattern: 1, n-2, 1
	# list.append some number that is at 

	# NCr = (NCr - 1 * (N - r + 1)) / r where 1 ≤ r ≤ N


# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Testing code
print(generate(5))
print(generate(1))