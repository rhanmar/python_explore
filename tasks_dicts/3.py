# setdefault and defaultdict


def collect_indexes(items):
	result = {}
	for key in items:
		# result.setdefault(k, 0).+=1
		result[key] = result.get(key, 0) + 1
	print result
	return result


def collect_indexes_2(items):
	from collections import defaultdict
	result = defaultdict(int)
	for key in items:
		result[key] += 1
	print result
	return result

d = collect_indexes("hello")
d_2 = collect_indexes_2("hello")
