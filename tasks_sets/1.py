# sets

def all_unique(iterable):
	items = list(iterable)
	return len(items) == len(set(items))

print all_unique("cat") # True
print all_unique([1, 2, 3]) # True
print all_unique([1, 2, 1]) # False
print all_unique({1,1,2})


print {1,2,2}