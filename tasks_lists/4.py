#slices

def rotated_left(items):
	return items[1:] + items[:1]

def rotated_right(items):
	return items[-1:] + items[:-1]


print rotated_left("ABCD") # "BCDA"

print rotated_right([1, 2, 3, 4]) # [4, 1, 2, 3]

