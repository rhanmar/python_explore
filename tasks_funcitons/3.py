# keyword arguments

def updated(source, **kwargs):
	new_source = source.copy()
	new_source.update(kwargs)
	return new_source



d = {'a': 1, 'b': False}
updated(d, a=2, b=True, c=None) # {'a': 2, 'b': True, 'c': None}
print(d) # {'a': 1, 'b': False}
print (updated(d) == d) # True
print (updated(d) is d) # False