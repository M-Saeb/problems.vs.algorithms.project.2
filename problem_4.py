def sort_012(input_list):
	"""
	Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

	Args:
		input_list(list): List to be sorted
	"""
	result = input_list.copy()
	# I used a variable to set the pointers for 0's & 2's
	# The 1's will automatically sit in the right position
	next_pos_0 = 0
	next_pos_2 = len(result) - 1

	front_index = 0

	while front_index <= next_pos_2:
		if result[front_index] == 0:
			result[front_index] = result[next_pos_0]
			result[next_pos_0] = 0
			next_pos_0 += 1
			front_index += 1
		elif result[front_index] == 2:           
			result[front_index] = result[next_pos_2] 
			result[next_pos_2] = 2
			next_pos_2 -= 1
		else:
			front_index += 1

	return result

def test_function(test_case):
	sorted_array = sort_012(test_case)
	print(sorted_array)
	if sorted_array == sorted(test_case):
		print("Pass")
	else:
		print("Fail")

test_function([])
test_function([0, 0, 0, 0])
test_function([2, 2, 2, 2, 1])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])