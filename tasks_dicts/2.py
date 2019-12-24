def count_all(items):
	result = {}
	for value in items:
		if (not value in result):
			result[value] = 1
		else:
			result[value] += 1
	return result

print count_all(["cat", "dog", "cat"]) # {"cat": 2, "dog": 1}
print count_all("hello") # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print count_all("*" * 20) # {'*': 20}
