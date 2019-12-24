def apply_diff(set_for_update, diff):
	add = set(diff['add'])
	remove = set(diff['remove'])

	set_for_update.update(add)
	set_for_update.difference_update(remove)


target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}
apply_diff(target, diff)
print target # {'c', 'b'}