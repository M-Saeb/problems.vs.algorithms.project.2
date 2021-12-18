def sqrt(number):
	"""
	Calculate the floored square root of a number

	Args:
		number(int): Number to find the floored squared root
	Returns:
		int: Floored Square Root
	"""
	if number < 0:
		return None

	if number in [0, 1]:
		return number

	mid = number // 2
	test_range = range(1, mid)
	for i in test_range:
		if number // i == i:
			return i			

print ("Pass" if  (None == sqrt(-1)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")