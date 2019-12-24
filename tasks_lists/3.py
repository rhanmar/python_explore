def rotate(items):
	if items:
		#last_value = items.pop()
		items.insert(0, items.pop(-1))


l = [1,2,3,4,5]
rotate(l)
print l