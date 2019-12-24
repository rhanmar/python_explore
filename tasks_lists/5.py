#for loop

def find_index(value, items):
	for (i, element) in enumerate(items):
		if element == value:
			return i
	#else:
	#	return None


print find_index('t', 'cat') # 2
print find_index(5, [1, 2, 3, 4, 5, 6, 7]) # 4
print find_index(42, []) is None # True
print find_index('!', 'abc') is None # True