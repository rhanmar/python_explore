def toggle(flag, flag_set):
	if (flag in flag_set):
		flag_set.discard(flag)
	else:
		flag_set.add(flag)


READ_ONLY = 'read_only'
flags = set()
toggle(READ_ONLY, flags)
print READ_ONLY in flags # True
toggle(READ_ONLY, flags)
print READ_ONLY in flags # False


def toggled(flag, flag_set):
	new_set = flag_set.copy()
	toggle(flag, new_set)
	return new_set
	'''
	if (flag in flag_set):
					return set()
				else:
					return {flag}
					'''


READ_ONLY = 'read_only'
flags = set()
new_flags = toggled(READ_ONLY, flags)
print READ_ONLY in flags # False
print READ_ONLY in new_flags # True