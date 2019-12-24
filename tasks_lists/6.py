# iterators and generators

def find_index(value, items):
	for (i, element) in enumerate(items):
		if element == value:
			return i

def find_second_index(value, items):
	iterator = iter(items)
	first = find_index(value, iterator)
	second = find_index(value, iterator)
	if (second):
		return first + second + 1 # + 1 because iterator always starts from 0

	else:
		return None

print find_second_index('b', 'bob') # 2

print find_second_index('a', 'cat') is None # True

print find_second_index('o', 'OoOOOOo') # 6