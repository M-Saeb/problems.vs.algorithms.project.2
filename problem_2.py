def rotated_array_search(input_list, number):
	"""
	Find the index by searching in a rotated sorted array

	Args:
		input_list(array), number(int): Input array to search and the target
	Returns:
		int: Index or -1
	"""
	if len(input_list) < 1:
		return -1

	# because we are search a rotated array, this just means we are searching a regular sorted array with negetive
	# so I just need to start at index = 0 and raise or lower the index to find the searched value
	# python negetive indexes came really handy in here
	index = 0
	while True:
		if input_list[index] == number:
			# this condition is to return the equivalent positive number of a nagetive index
			if index < 0:
				return index + len(input_list)
			else:
				return index

		elif input_list[index] > number:
			index -= 1

		else:
			# if the next elemnent is not bigger than the current element
			# that means the element doesn't exist
			if input_list[index] > input_list[index+1]:
				return -1
			else:
				index += 1


def linear_search(input_list, number):
	for index, element in enumerate(input_list):
		if element == number:
			return index
	return -1

def test_function(test_case):
	input_list = test_case[0]
	number = test_case[1]
	if linear_search(input_list, number) == rotated_array_search(input_list, number):
		print("Pass")
	else:
		print("Fail", linear_search(input_list, number), rotated_array_search(input_list, number))

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])