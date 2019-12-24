'''
sort tuple in ascending order
'''

def sort_pair(pair):
	(first, second) = pair
	return pair if first < second else (second, first)


print(sort_pair((2,1)))
print(sort_pair((2,11)))