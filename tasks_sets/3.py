def diff_keys(iterable1, iterable2):
	old_keys = set(iterable1)
	new_keys = set(iterable2)
	return {
	'kept': old_keys & new_keys,
	'added': new_keys - old_keys,
	'removed': old_keys - new_keys
	}


print diff_keys({'name': 'Bob', 'age': 42}, {}) # {'kept': set(), 'added': set(), 'removed': {'name', 'age'}}
print diff_keys({}, {'name': 'Bob', 'age': 42}) # {'kept': set(), 'added': {'name', 'age'}, 'removed': set()}
print diff_keys({'a': 2}, {'a': 1}) # {'kept': {'a'}, 'added': set(), 'removed': set()}