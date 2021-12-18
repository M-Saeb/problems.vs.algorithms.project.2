def rearrange_digits(input_list):
	"""
	Rearrange Array Elements so as to form two number such that their sum is maximum.

	Args:
		input_list(list): Input List
	Returns:
		(int),(int): Two maximum sums
	"""
	if len(input_list) < 1:
		return [0, 0]

	# sense we know that our input cases are 0 to 9, I created a list that'll contian the number of times
	# each digit existed in the input list from biggest to smallest
	# (ex: [8, 6 ,8, 3], the mapped will contain [0, 0, 0, 1, 0, 0, 1, 0, 2, 0])
	# (ex:    [9, 0, 2], the mapped will contain [1, 0, 1, 0, 0, 0, 0, 0, 0, 1])
	# (ex: [7, 3, 7, 4], the mapped will contain [0, 0, 0, 1, 1, 0, 0, 2, 0, 0])
	list_mapper = [0 for _ in range(10)]
	for item in input_list:
		list_mapper[item] += 1

	num1 = ""
	num2 = ""

	index = 9 # start from the beggist number
	while any(list_mapper):
		if list_mapper[index] > 0:
			if len(num1) > len(num2):
				num2 = num2 + str(index)
			else:
				num1 = num1 + str(index)

			list_mapper[index] -= 1

		else:
			index -= 1

	return [int(num1), int(num2)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail", sum(output), sum(solution))

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 5, 7, 4], [74, 51]])
test_function([[1, 2], [1, 2]])
test_function([[3, 3, 3, 3, 3], [333, 33]])
test_function([[], [0 , 0]])
