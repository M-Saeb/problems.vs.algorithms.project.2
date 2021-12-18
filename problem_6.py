## Example Test Case of Ten Integers
import random

def get_min_max(ints):
	"""
	Return a tuple(min, max) out of list of unsorted integers.

	Args:
		ints(list): list of integers containing one or more integers
	"""
	if len(ints) < 1:
		return ()
	
	# first thing I did is define the first element as both the Minmum & the Maximum of the list
	min = ints[0]
	max = ints[0]

	# Than I looped over the list and changed the min & max according to the elements
	for num in ints[1:]:
		if num < min:
			min = num
		if num > max:
			max = num

	return (min, max)

test1 = [i for i in range(0, 20)]  # a list containing 0 - 19
random.shuffle(test1)

print ("Pass" if ((0, 19) == get_min_max(test1)) else "Fail")
print ("Pass" if (() == get_min_max([])) else "Fail")
print ("Pass" if ((2 , 2) == get_min_max([2])) else "Fail")