from math import sqrt

def get_square_roots(n):
	if n < 0:
		#something
		return []
	elif n == 0:
		return [sqrt(n)]
	else:
		return [-sqrt(n), sqrt(n)]


def get_range(n):
	l = []
	i = 0
	while i < n:
		l.append(i)
		i += 1 
	return l

print get_square_roots(9)
print get_range(10)

